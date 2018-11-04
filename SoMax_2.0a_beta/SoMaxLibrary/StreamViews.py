import Atom, Tools, Events, ActivityPatterns, MemorySpaces
from copy import deepcopy
from MergeActions import *


# The StreamView object is a container that manages several atoms, whose activity
#   patterns are taken and then mixed. This is mainly motivated to modulate the diverse
#   activity patterns depending on the transformations.

class StreamView(object):
    def __init__(self, name="streamview", weight=1.0, atoms=dict(), merge_actions = [DistanceMergeAction()]):
        self.name = name
        # merge actions list
        self.merge_actions = []
        if type(merge_actions)!=list:
             merge_actions = list(merge_actions)
        for m_a in merge_actions:
            self.merge_actions.append(m_a)
        # atoms dictionary
        self.atoms = dict()

        # streamview weight
        self.weight = weight
        if atoms!=dict():
            if type(atoms)==list:
                for atom in atoms:
                    self.atoms[str(atom.name)] = atom
            elif type(atoms)==dict:
                self.atoms = dict(atoms)

    def __repr__(self):
        return "Stream view called {0} with atoms {1}".format(self.name, self.atoms)

    def create_atom(self, path="atom", weight=1.0, \
                    label_type = Events.AbstractLabel, contents_type=Events.AbstractContents, event_type=Events.AbstractEvent, \
                    activity_type = ActivityPatterns.ClassicActivityPattern, memory_type = MemorySpaces.NGramMemorySpace,
                    memory_file = None):
        '''creating an atom at required path'''
        atom = None
        if ":" in path:
            head, tail = Tools.parse_path(path) # if atom in a sub-streamview
            atom = self.atoms[head].add_atom(tail, weight, label_type, contents_type, event_type, activity_type, memory_type)
            print "[ERROR] Could not add atom {0} in streamview {1}".format(path, self.name)

        else:
            # if atom is directly in current streamview
            if path in self.atoms:
                print "[ERROR] Atom {0} already existing in {1}".format(path, self.name)
            else:
                atom = Atom.Atom(path, weight, label_type, contents_type, event_type, activity_type, memory_type, memory_file)
                self.atoms[path] = atom
        return atom


    def create_streamview(self, path="streamview", weight=1.0, atoms=dict(), merge_actions = [DistanceMergeAction]):
        '''creating a streamview at required path'''
        if ":" in path:
            # if streamview in sub-streamview
            head, tail = Tools.parse_path(path)
            st = self.atoms[head].create_streamview(tail, weight, atoms, merge_actions)
        else:
            # if streamview directly in current streamview
            st = StreamView(path, weight, atoms, merge_actions)
            self.atoms[path] = st
        return st



    def add_atom(self, atom, name=None, copy=False, replace=False):
        '''add an existing atom in the current streamview'''
        if name==None:
            name=atom.name
        if name in self.atoms.keys():
            if not replace:
                raise Exception("{0} already exists in {1}".format(atom.name, self.name))
        if copy:
            self.atoms[name] = atom.copy(name)
        else:
            self.atoms[name] = atom

    def get_atom(self, name, copy=False):
        '''fetching an atom'''
        path, path_bottom = Tools.parse_path(name)
        if path_bottom!=None and path in self.atoms.keys():
            return self.atoms[path].get_atom(path_bottom)
        elif path_bottom==None and path in self.atoms.keys():
            return self.atoms[path]
        else:
            return None

    def delete_atom(self, name):
        '''deleting an atom'''
        if not ":" in name:
            del self.atoms[name]
        else:
            head, tail = Tools.parse_path(name)
            self.atoms[name].delete_atom(tail)


    def influence(self, path, time, *data, **kwargs):
        '''influences all sub-atoms with data'''
        if path==None or path=="":
            for atom in self.atoms.values():
                atom.influence(time, *data)
        else:
            pf, pr = Tools.parse_path(path)
            if pf in self.atoms.keys():
                if isinstance(self.atoms[pf], Atom.Atom):
                    self.atoms[pf].influence(time, *data, **kwargs)
                elif isinstance(self.atoms[pf], StreamViews.StreamView):
                    self.atoms[pf].influence(pr, time, *data, **kwargs)

    def read(self, path, filez):
        '''read all sub-atoms with data'''
        print path
        if path==None:
            for n,a in self.atoms.iteritems():
                if issubclass(type(a), Atom.Atom):
                    a.read(filez)
                else:
                    a.read(None, filez)
        else:
            path, path_follow = Tools.parse_path(path)
            if path_follow==None:
                for atom in self.atoms.values():
                    atom.read(filez)
            elif path in self.atoms.keys():
                if isinstance(self.atoms[path_follow], StreamView):
                    self.atoms[path_follow].read(path_follow, filez)
                else:
                    self.atoms[path_follow].read(filez)
            else:
                raise Exception("Atom or streamview {0} missing!".format(path))


    def get_activities(self, date, path=None, weighted=True):
        '''get separated activities of children'''
        if path!=None:
            if ':' in path:
                head, tail = Tools.split_path(head, tail)
                activities = self.atoms[head].get_activities(date, path=tail)
            else:
                activities = self.atoms[path].get_activities(date)
        else:
            activities = dict()
            for name, atom in self.atoms.iteritems():
                activities[name] = atom.get_merged_activity(date, weighted=weighted)
        if issubclass(type(activities), Tools.SequencedList):
            activities = {path:activities}
        return activities

    def get_merged_activity(self, date, weighted=True):
        '''get merged activities of children'''
        weight_sum = float(reduce(lambda x, y: x+y.weight, self.atoms.values(), 0.0))
        merged_activity = SequencedList()
        for atom in self.atoms.values():
            w = atom.weight if weighted else 1.0
            merged_activity = merged_activity + atom.get_activity(date).mul(w, 0)
        for merge_action in self.merge_actions:
            merged_activity = merge_action.merge(merged_activity)
        return merged_activity


    def set_weight(self, path, weight):
        '''set weight of atom addressed at path'''
        if not ":" in path:
            self.atoms[path].set_weight(weight)
        else:
            head, tail = parse_path(atom)
            self.atoms[head].set_weight(tail, weight)

    def get_info_dict(self):
        '''returns info dictionary'''
        infodict = {"activity type":str(type(self)), "weight":self.weight, "type":"Streamview"}
        infodict["atoms"]=dict()
        for a,v in self.atoms.iteritems():
            infodict["atoms"][a]=v.get_info_dict()
        return infodict

    def reset(self, time):
        for f in self.atoms.values():
            f.reset(time)

    def test(self, coucou):
        print "coucou!!!"
