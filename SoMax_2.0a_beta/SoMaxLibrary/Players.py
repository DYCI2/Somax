
import StreamViews, Tools, Events, ActivityPatterns, MemorySpaces, Transforms
import sys, inspect, importlib, operator, itertools, random, json, os, re
import numpy as np
from collections import deque, OrderedDict
import Transforms
from MergeActions import *
from OSC import OSCClient, OSCMessage


###############################################################################
# Player is the main generation unit in SoMax.
# it is roughly composed by three different parts :
#       - generation units : all streamviews in the self.streamviews dictionary,
#           which return their activity profile to guide the event generation
#       - decision units : "decide" functions that selects the event to generate
#           given a set of activity profiles
#       - communication units : connecting with Max, external compatibility


class Player(object):
    max_history_len = 100
    def __init__(self, name, scheduler, out_port):
        self.name = name #name of the player
        self.scheduler = scheduler # server scheduler
        self.streamviews = dict() # streamviews dictionary
        self.improvisation_memory = deque('', self.max_history_len)
        self.decide = self.decide_chooseMax # current decide function
        self.merge_actions =[DistanceMergeAction(), PhaseModulationMergeAction(self.scheduler)] # final merge actions

        # current streamview is the private streamview were is caught the
        #    generation atom, from which events are generated and is auto-influenced
        self.current_streamview=StreamViews.StreamView(name="auto_streamview")
        self.current_atom = None
        self.self_influence = True
        self.nextstate_mod = 1.5
        self.waiting_to_jump = False

        self.info_dictionary = dict()
        self.client = OSCClient()
        self.out_port = out_port
        print "[INFO] Player", name, "created with outcoming port", out_port



    ######################################################
    ###### GENERATION AND INFLUENCE METHODS

    def new_event(self, date, event_index=None):
        '''returns a new event'''

        # if not any memory is loaded
        if not "_self" in self.current_streamview.atoms.keys():
            return None

        # if event is specified, play it now
        if event_index!=None:
            self.reset()
            event_index = int(event_index)
            z_, event = self.current_streamview.atoms["_self"].memorySpace[event_index]
            # using actual transformation?
            transforms = [Transforms.NoTransform()]
            self.waiting_to_jump = False
        else:
            # get global activity
            global_activity = self.get_merged_activity(date, merge_actions=self.merge_actions)

            # if going to jump, erases peak in neighbour event
            if self.waiting_to_jump:
                zetas = global_activity.get_dates_list()
                states, _ = self.current_streamview.atoms["_self"].memorySpace.get_events(zetas)
                for i in range(0, len(states)):
                    if states[i].index == self.improvisation_memory[-1][0].index+1:
                        del global_activity[i]
                self.waiting_to_jump = False

            if len(global_activity)!=0 and len(self.improvisation_memory)>0:
                event, transforms = self.decide(global_activity)
                if event==None:
                    # if no event returned, choose default
                    event, transforms = self.decide_default()
                if type(transforms)!=list:
                    transforms = [transforms]
            else:
                # if activity is empty, choose default
                event, transforms = self.decide_default()
            for transform in transforms:
                event = transform.decode(event)
        # add event to improvisation memory
        self.improvisation_memory.append((event, transforms))
        # influences private streamview if auto-influence activated
        if self.self_influence:
            self.current_streamview.influence("_self", date, event.get_label())
        # sends state num
        self.send([event.index, event.get_contents().get_zeta(), event.get_contents().get_state_length()], "/state")
        return event

    def new_content(self, date):
        ''' returns new contents'''
        event = new_event(date)
        return event.get_contents().get_contents()


    def influence(self, path, *args, **kwargs):
        '''influences target atom with *args'''
        time = self.scheduler.get_time()
        pf, pr = Tools.parse_path(path)
        if pf in self.streamviews.keys():
            self.streamviews[pf].influence(pr, time, *args, **kwargs)
        else:
            raise Exception("[ERROR] Streamview {0} is missing".format(pf))

    def jump(self):
        self.waiting_to_jump = True

    def goto(self, state = None):
        self.pending_event = state





    ######################################################
    ###### UNIT GENERATION AND DELETION

    def create_streamview(self, name="streamview", weight = 1.0, merge_actions = [DistanceMergeAction()]):
        '''creates streamview at target path'''
        if not ":" in name:
            st = StreamViews.StreamView(name=name, weight=weight, merge_actions = merge_actions)
            self.streamviews[name] = st
        else:
            path_splitted=name.split(":")
            path = path_splitted[0]
            path_bottom = reduce(lambda x,y: x+":"+y, path_splitted[1:])
            if path in self.streamviews:
                print "[ERROR] streamview {0} already exists in player"
            else:
                self.streamviews[path].create_streamview(path_bottom, weight, merge_actions=merge_actions)
        print "[INFO] streamview {0} created!".format(name)
        self.send_info_dict()

    def create_atom(self, name, weight=1.0, \
                    label_type = Events.AbstractLabel, contents_type=Events.AbstractContents, event_type=Events.AbstractEvent, \
                    activity_type = ActivityPatterns.ClassicActivityPattern, memory_type = MemorySpaces.NGramMemorySpace, memory_file = None):
        '''creates atom at target path'''
        if not ":" in name:
            raise Exception("[ERROR] Atoms must be embedded in a streamview first!")
        path, path_bottom = Tools.parse_path(name)
        atom = self.streamviews[path].create_atom(path_bottom, weight, label_type, contents_type, event_type, activity_type, memory_type, memory_file)
        if not "_self" in self.current_streamview.atoms or name==self.current_atom:
            self.set_active_atom(name)
            self.current_atom = name
        if atom != None:
            print "[INFO] atom {0} created!".format(name)
            self.send_info_dict()

    def delete_atom(self, name):
        '''deletes target atom'''
        if not ":" in name:
            del self.streamviews[name]
        else:
            head, tail = Tools.parse_path(name)
            self.streamviews[head].delete_atom(tail)
        print "[INFO] atom {0} deleted!".format(name)
        self.send_info_dict()

    def read_file(self, path, filez):
        '''tells target atom to read corresponding file.'''
        # read commands to a streamview diffuses to every child of this streamview
        if path==None:
            for n,s in self.streamviews.iteritems():
                s.read(None, filez)
            self.current_streamview.read(None, filez)
        elif path=="_self":
            self.current_streamview.read("_self", filez)
        else:
            path_head, path_follow = Tools.parse_path(path)
            if path_head in self.streamviews.keys():
                self.streamviews[path_head].read(path_follow,filez)
                if path==self.current_atom:
                    self.current_streamview.atoms["_self"].read(filez)
            else:
                raise Exception("[ERROR] Streamview {0} missing!".format(path))
        # if target atom is current atom, tells private atom to read the file
        if self.current_atom == path:
            self.streamviews.atoms["_self"].read(filez)
        self.update_memory_length()
        self.send_info_dict()


    def set_active_atom(self, name):
        '''set private atom of the player to target'''
        path, path_bottom = Tools.parse_path(name)
        if path in self.streamviews.keys():
            atom = self.streamviews[path].get_atom(path_bottom)
        else:
            atom=None
        if atom!=None:
            if "_self" in self.current_streamview.atoms:
                del self.current_streamview.atoms["_self"]
            self.current_streamview.add_atom(atom, copy=True, replace=True, name="_self")
        else:
            raise Exception("Could not find atom {0}!".format(name))
        if self.current_atom != None:
            path, path_bottom = Tools.parse_path(self.current_atom)
            if path in self.streamviews.keys():
                former_atom = self.streamviews[path].get_atom(path_bottom)
                former_atom.active = False
        self.current_atom = name
        if issubclass(atom.memorySpace.contents_type, Events.ClassicAudioContents):
            self.send_buffer(atom)
        atom.active = True
        print "[INFO] Setting active atom to {0} ".format(name)
        self.update_memory_length()
        self.send_info_dict()


    ######################################################
    ###### ACTIVITIES ACCESSORS

    def get_activities(self, date, path=None, weighted = True):
        '''fetches separated activities of the children of target path'''
        if path!=None:
            if ":" in path:
                head, tail = Tools.parse_path(path)
                activities = self.streamviews[head].get_activities(date, path=tail)
            else:
                activities = self.streamviews[path].get_activities(date, path=None)
        else:
            activities = dict()
            for n,a in self.streamviews.iteritems():
                w = a.weight if weighted else 1.0
                activities[n] = a.get_merged_activity(date, weighted=weighted).mul(w,0)
            if "_self" in self.current_streamview.atoms:
                w = self.current_streamview.weight if weighted else 1.0
                activities["_self"] = self.current_streamview.get_merged_activity(date, weighted=weighted).mul(w,0)
        return activities

    def get_merged_activity(self, date, weighted=True, filters=None, merge_actions=[StreamViews.DistanceMergeAction()]):
        '''getting activites of all streamviews of the player, merging with corresponding merge actions and optionally weighting'''
        global_activity = Tools.SequencedList()
        weight_sum = self.get_weights_sum()
        if filters==None:
            filters = self.streamviews.keys()
        for f in filters:
            activity = self.streamviews[f].get_merged_activity(date, weighted=weighted)
            w = self.streamviews[f].weight/weight_sum if weighted else 1.0
            global_activity = global_activity + activity.mul(w, 0)
        si_w = self.current_streamview.weight/weight_sum if weighted else 1.0
        global_activity = global_activity + self.current_streamview.get_merged_activity(date, weighted=True).mul(si_w, 0)
        for m in merge_actions:
            global_activity = m.merge(global_activity)
        return global_activity

    def reset(self, time=None):
        '''reset improvisation memory and all sub-streamview'''
        time = time if time!=None else self.scheduler.time
        self.improvisation_memory = deque('', self.max_history_len)
        self.current_streamview.reset(time)
        for s in self.streamviews.keys():
            self.streamviews[s].reset(time)

    def get_weights_sum(self):
        '''getting sum of subweights'''
        p = reduce(lambda x,y: x+y.weight, self.streamviews.values(), 0.0)
        if self.current_streamview.atoms["_self"]:
            p+=self.current_streamview.atoms["_self"].weight
        return p



    '''def update_info_dictionary(self):
        if self.streamviews!=dict():
            self.info_dictionary["streamviews"] = OrderedDict()
            tmp_dic = dict()
            for k,v in self.streamviews.iteritems():
                tmp_dic[k] = dict()
                tmp_dic[k]["class"] = v[0].__desc__()
                tmp_dic[k]["weight"] = v[1]
                tmp_dic[k]["file"] = v[2]
                tmp_dic[k]["size"] = v[0].get_length()
                tmp_dic[k]["length_beat"] = v[0].metadata["duration_b"]
                if k==self.current_streamview:
                    self.info_dictionary["streamviews"][k] = dict(tmp_dic[k])
            for k,v in tmp_dic.iteritems():
                if k!=self.current_streamview:
                    self.info_dictionary["streamviews"][k] = dict(tmp_dic[k])
        else:
            self.info_dictionary["streamviews"] = "empty"
        self.info_dictionary["current_streamview"] = str(self.current_streamview)'''

    ######################################################
    ###### EXTERNAL METHODS


    def send_buffer(self, atom):
        ''' sending buffers in case of audio contents'''
        filez = atom.memorySpace.current_file
        with open(filez) as f:
            name, _ = os.path.splitext(filez)
            name = name.split('/')[-1]
            g = os.walk('../')
            filepath = None
            for r,d,fs in g:
                for f in fs:
                    n,e = os.path.splitext(f)
                    if n==name and e!='.json':
                        filepath = r+'/'+f
            if filepath!=None:
                self.send('buffer '+ os.path.realpath(filepath))
            else:
                raise Exception("[ERROR] couldn't find audio file associated with file", filez)

    def set_self_influence(self, si):
        self.self_influence = bool(si)

    def set_nextstate_mod(self, ns):
        self.nextstate_mod = ns

    def update_memory_length(self):
        '''sending active memory length'''
        atom = self.current_streamview.atoms["_self"]
        print atom
        if len(atom.memorySpace)>0:
            lastEvent = atom.memorySpace[-1][1]
            length = lastEvent.get_contents().get_zeta() + lastEvent.get_contents().get_state_length()
            self.send(length, "/memory_length")

    def get_info_dict(self):
        '''returns the dictionary containing all information of the player'''
        infodict = {"decide": str(self.decide), "self_influence": str(self.self_influence), "port":self.out_port}
        try:
            infodict["current_file"] = str(self.current_streamview.atoms["_self"].current_file)
        except:
            pass
        infodict["streamviews"] = dict()
        for s,v in self.streamviews.iteritems():
            infodict["streamviews"][s] = v.get_info_dict()
            infodict["current_atom"] = self.current_atom
        infodict["current_streamview"] = self.current_streamview.get_info_dict()
        if self.current_streamview.atoms!=dict():
            if len(self.current_streamview.atoms["_self"].memorySpace)!=0:
                self_contents = self.current_streamview.atoms["_self"].memorySpace[-1][1].get_contents()
                infodict["current_streamview"]["length_beat"] = self_contents.get_zeta("relative")+self_contents.get_state_length("relative")
                infodict["current_streamview"]["length_time"] = self_contents.get_zeta("absolute")+self_contents.get_state_length("absolute")
        infodict["subweights"] = self.get_normalized_subweights()
        infodict["nextstate_mod"] = self.nextstate_mod
        infodict["phase_selectivity"] = self.merge_actions[1].selectivity
        infodict["triggering_mode"] = self.scheduler.triggers[self.name]
        return infodict

    def send_info_dict(self):
        '''sending the info dictionary of the player'''
        infodict = self.get_info_dict()
        str_dic = Tools.dic_to_strout(infodict)
        self.send("clear", "/infodict")
        self.send(self.streamviews.keys(), "/streamviews")
        for s in str_dic:
            self.send(s, "/infodict")
        self.send(self.name, "/infodict-update")
        print "[INFO] Updating infodict for player", self.name

    def set_weight(self, streamview, weight):
        '''setting the weight at target path'''
        if not ":" in streamview:
            if streamview!="_self":
                self.streamviews[streamview].weight = weight
            else:
                self.current_streamview.atoms["_self"].weight =  weight
        else:
            head, tail = Tools.parse_path(streamview)
            self.streamviews[head].set_weight(tail, weight)
        self.send_info_dict()
        return True

    def get_normalized_subweights(self):
        weights = [];
        weight_sum = 0;
        for s in self.streamviews.values():
            weights.append(s.weight)
            weight_sum = weight_sum + s.weight
        return map(lambda x: x/weight_sum, weights)



    ######################################################
    ###### DECIDING METHODS

    def decide_default(self):
        '''default decision method : selecting conjoint event'''
        if len(self.improvisation_memory)!=0:
            previousState = self.improvisation_memory[-1][0]
            new = self.current_streamview.atoms["_self"].memorySpace[(previousState.index+1)%len(self.current_streamview.atoms["_self"].memorySpace)]
            trans = self.improvisation_memory[-1][1]
        else:
            new = self.current_streamview.atoms["_self"].memorySpace[0]
            trans = [Transforms.NoTransform()]
        return new[1], trans

    def decide_chooseMax(self, global_activity):
        '''choosing the state with maximum activity'''
        zetas = global_activity.get_dates_list()
        states, _ = self.current_streamview.atoms["_self"].memorySpace.get_events(zetas)
        v_t = global_activity.get_events_list()
        v = map(lambda x: x[0], v_t)
        for i in range(1, len(states)):
            if not states[i] is None:
                if states[i].index == self.improvisation_memory[-1][0].index+1:
                    v[i]*=self.nextstate_mod
        sorted_values = sorted( list(zip(v, range(len(v)))), key = operator.itemgetter(0), reverse = True)
        max_value = sorted_values[0][0]
        maxes = [n for n in itertools.takewhile(lambda x: x[0] == max_value, sorted_values)]
        next_state_index = random.choice(maxes)
        next_state_index = next_state_index[1]
        next_state, distance = self.current_streamview.atoms["_self"].memorySpace.get_events(zetas[next_state_index])
        return next_state[0], v_t[next_state_index][1]

    ######################################################
    ###### OSC METHODS

    def send(self, content, address=None):
        if address==None:
            address = "/"+self.name
        message = OSCMessage(address)
        message.append(content)
        self.client.sendto(message, ("127.0.0.1", self.out_port))


    # Formatting incoming to Python
    def process_contents(self, ct):
        if ct=='True':
            return True
        elif ct=='False':
            return False
        elif ct=='None':
            return None
        return ct

    def get(self, path_contents):
        if path_contents == None:
            return self
        if path_contents[0]=="#":
            current_obj = getattr(Transforms, path_contents[1:])
            return current_obj

        assert(len(path_contents)>1)
        current_obj = self
        for i in range(0, len(path_contents)):
            if i==0:
                current_obj = current_obj.streamviews[path_contents[i]]
            else:
                current_obj = current_obj.atoms[path_contents[i]]
        return current_obj

    def getargs(self, contents):
        args = []
        kargs = dict()
        for u in contents:
            try:
                if "." in u:
                    u = float(u)
                else:
                    u = int(u)
            except:
                pass
            if type(u)==str and "=" in u:
                key, value = u.split("=")
                value = str.replace(value, "%20", " ")
                kargs[key] = self.process_contents(value)
            else:
                args.append(u)
        args = map(self.process_contents, args)
        return args, kargs

    # Communication protocol
    def connect(self, msg, id, contents, ports):
        if len(contents)==0:
            return
        header = contents[0]
        vals = None
        path = None
        attributes = None
        # start splitting command
        if "=" in header:
            header, vals = header.split("=")
        if header[0]==":":
            paths = header.split(":")
            path = paths[1:-1] + [paths[-1].split(".")[0]]
            attributes = paths[-1].split(".")[1:]
        else:
            if header[0]!="#":
                path = None
                attributes = header.split(".")
            else:
                things = header.split(".")
                path = things[0]
                attributes = things[1:]
        # target object (None for Player, :path:to:stream/atom for sub-atoms)
        obj = self.get(path)
        it_range = range(0, len(attributes)-1) if vals!=None else range(0, len(attributes))
        for i in it_range:
            current_attribute = attributes[i]
            name, key = re.match(r"([\w]+)(\[.+\])?", current_attribute).groups()
            obj = getattr(obj, name)
            if key:
                key = key[1:-1]
                try:
                    key = int(key)
                except:
                    pass
                obj = obj[key]
        if vals==None:
            if callable(obj):
                args, kargs = self.getargs(contents[1:])
                result = obj(*args, **kargs)
        else:
            vals = vals.split(",")
            vals, _ = self.getargs(vals)
            vals = vals[0] if len(vals)==1 else vals
            setattr(obj, attributes[-1], vals)
