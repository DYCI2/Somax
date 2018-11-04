import ActivityPatterns
import MemorySpaces
import Events
from copy import copy
# Atom is the core object that contains an activity pattern and a memory space.
# He basically does two things : managing influences and updating activity.

class Atom(object):
    def __init__(self, name="atom", weight=1.0, \
                    label_type = Events.AbstractLabel, contents_type=Events.AbstractContents, event_type=Events.AbstractEvent, \
                    activity_type = ActivityPatterns.ClassicActivityPattern, memory_type = MemorySpaces.NGramMemorySpace, memory_file = None):
        self.weight=weight # set the weightt
        if type(activity_type)==str:
            activity_type = getattr(ActivityPatterns, activity_type)
        if type(memory_type)==str:
            memory_type = getattr(MemorySpaces, memory_type)
        self.activity_type = activity_type
        self.activityPattern = activity_type() # creates activity
        self.label_type = label_type; self.contents_type = contents_type; self.event_type = event_type
        self.memory_type = memory_type
        self.memorySpace = memory_type(label_type = label_type, contents_type = contents_type, event_type = event_type) # create memory space
        self.name = name
        self.active = False
        if memory_file != None:
            self.read(memory_file, label_type=self.label_type, contents_type=self.contents_type, event_type=self.event_type)
        else:
            self.current_file = None

    def __repr__(self):
        return "Atom with {0} and {1}".format(type(self.activityPattern), type(self.memorySpace))

    # Tells the memory space to load the file filez
    def read(self, filez, memory_type=None, \
                label_type = Events.AbstractLabel, contents_type=Events.AbstractContents, event_type=Events.AbstractEvent):
        if memory_type!=None:
            # if different memory type, create a new memory space
            memory_class = getattr(MemorySpaces, memory_type)
            self.memorySpace = memory_class(label_type = label_type, contents_type = contents_type, event_type = event_type)
        # read file
        print "[INFO] reading file", filez, "..."
        success = self.memorySpace.read(filez)
        if success == False:
            raise Exception("[ERROR] failed to load the file ", filez)
        else:
            print "[INFO] file {0} loaded".format(filez)
        # set current file
        self.current_file = filez

    # set current weight of atom
    def set_weight(self, weight):
        self.weight = float(weight)

    # influences the memory with incoming data
    def influence(self,time,*data,**kwargs):
        peaks = self.memorySpace.influence(data, **kwargs) # we get the activity peaks created by influence
        if peaks!=[]:
            self.activityPattern.update_activity(time) # we update the activity profile to the current time
            self.activityPattern.insert(*peaks) # we insert the peaks into the activity profile


    # external method to get back atom's activity
    def get_activity(self, date, weighted=True):
        w = self.weight if weighted else 1.0
        activity = self.activityPattern.get_activity(date)
        # returns weighted activity
        return activity.mul(w, 0)

    # sugar
    def get_activities(self, date, weighted=True):
        return self.get_activity(date, weighted)

    def get_merged_activity(self, date, weighted = True):
        return self.get_activity(date, weighted)

    # own copy method
    def copy(self, name):
        atom =  Atom(name=name, weight = self.weight, \
                        label_type = self.memorySpace.label_type, contents_type=self.memorySpace.contents_type, event_type=self.memorySpace.event_type, \
                        activity_type = self.activity_type, memory_type = self.memory_type)
        atom.memorySpace = self.memory_type(self.memorySpace.get_dates_list(), self.memorySpace.get_events_list(),label_type = self.memorySpace.label_type, contents_type=self.memorySpace.contents_type, event_type=self.memorySpace.event_type)
        atom.current_file = self.current_file
        return atom

    # external method to fetch properties of the atom
    def get_info_dict(self):
        infodict= {"activity":self.activityPattern.__desc__(), "memory":self.memorySpace.__desc__(), \
                    "event_type":self.memorySpace.event_type.__desc__(), "label_type":self.memorySpace.label_type.__desc__(), \
                    "contents_type":self.memorySpace.contents_type.__desc__(), "name":self.name, "weight":self.weight, "type":"Atom", "active":self.active}
        if self.current_file!=None:
            infodict["current_file"]=str(self.current_file)
            infodict["length"]=len(self.memorySpace)
        else:
            infodict["current_file"]="None"
            infodict["length"]=0
        return infodict

    def isAvailable(self):
        return self.activityPattern.isAvailable() and self.memorySpace.isAvailable()

    def reset(self, time):
        self.activityPattern.reset(time)

    def settest(self, n):
        print n

    def test(self):
        print self.testVal, self.testArr, self.testDic
