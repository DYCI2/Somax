import numpy as np
import json, bisect, os
import Events
import Transforms
from Tools import SequencedList, intersect
from collections import deque
from copy import deepcopy

# overloading Memory object, asserting a sequence of Event objects and embedding
#    a given representation, with its influence function used by Atom objects


class AbstractMemorySpace(SequencedList):
    def __init__(self, dates=[], states=[], \
                    label_type = Events.AbstractLabel, contents_type=Events.AbstractContents, event_type=Events.AbstractEvent):
        SequencedList.__init__(self, dates, states)
        self.label_type = label_type
        self.contents_type = contents_type
        self.event_type = event_type
        if type(label_type)==str or type(contents_type)==str or type(event_type)==str:
            if type(label_type)==str:
                self.label_type = getattr(Events, label_type)
            if type(contents_type)==str:
                self.contents_type = getattr(Events, contents_type)
            if type(event_type)==str:
                self.event_type = getattr(Events, event_type)
        self.infos = dict()
        self.available = True

    def __repr__(self):
        return "AbstractActivityPattern"
        #print "maps the raw data from memory to its internal representation"

    def __desc__(self):
        return "Abstract Memory Space"

    def read(self, file, *args):
        return True # True if succeded, False if failed

    def append(self, date, *args):
        event = self.build_event(*args)
        SequencedList.append(self, date, event)
        # and then additional processing specific to the Memory Space

    def influence(self, event):
      #print "here, the memory influences its internal state and returns activity peaks"
        return [], [] # returns dates and activities

    def isAvailable(self):
        return bool(self.available) # securities

    # build event from external data
    def build_event(self, *args, **kwargs):
        label = self.label_type.get_label_from_data(*args, **kwargs)
        contents = self.contents_type.get_contents_from_data(*args, **kwargs)
        event = self.event_type(label, contents)
        event.index = len(self)
        return event

    def reset(self):
        pass

class NGramMemorySpace(AbstractMemorySpace):
    def __init__(self, dates=[], states=[], \
                    label_type = Events.AbstractLabel, contents_type=Events.AbstractContents, event_type=Events.AbstractEvent):
        AbstractMemorySpace.__init__(self, [], [], label_type, contents_type, event_type)
        self.ngram_size = 3
        self.subsequences = dict()
        self.buffer = deque([], self.ngram_size)
        self.current_file = None
        self.typeID = None
        self.transforms = [Transforms.NoTransform, Transforms.TransposeTransform]
        for i in range(0, min(len(dates), len(states))):
            self.append(dates[i], states[i])

    def __repr__(self):
        return "N-Gram based memory"

    def __desc__(self):
        return str(self.ngram_size)+"-NGram based memory space"

    # 26/09 : redefinir append et definir insert
    def append(self, date, *args):
        AbstractMemorySpace.append(self, date, *args)
        if len(self.orderedEventList)<self.ngram_size:
            return
        # adding n-plets to subsequences dict
        seq = self.orderedEventList[-(self.ngram_size):len(self.orderedEventList)]
        seq = tuple(map(lambda state: state.get_label(), seq))
        dic = dict(self.subsequences)
        if len(dic)==0:
            self.subsequences[seq] = [len(self.orderedEventList)-1]
        else:
            sub_keys = self.subsequences.keys()
            if seq in sub_keys:
                j = sub_keys.index(seq)
                self.subsequences[sub_keys[j]].append(len(self.orderedEventList)-1)
            else:
                self.subsequences[seq] = [len(self.orderedEventList)-1]

    def build_subsequences(self):
        if len(self)<self.ngram_size:
            return
        self.subsequences = dict()
        bufr = deque([], self.ngram_size)
        for z,v in self:
            bufr.append(v.get_label())
            if len(bufr)>=self.ngram_size:
                seq = tuple(bufr)
                try:
                    self.subsequences[seq].append(z)
                except:
                    self.subsequences[seq] = [z]
                    pass
        self.buffer = deque([], self.ngram_size)


    def influence(self, data, **kwargs):
        event = self.build_event(*data, **kwargs)
        self.buffer.append(event.get_label())
        transforms = []
        peaks = []
        valid_transforms = self.transforms # getting appropriate transformations
        for Transform in valid_transforms:
            transforms.extend(Transform.get_transformation_patterns())
        if len(self.buffer)>=self.ngram_size:
            for transform in transforms:
                k = tuple(map(lambda x: transform.encode(x), self.buffer))
                values = []
                c = None
                for t, z in self.subsequences.iteritems():
                    if k==t:
                        c=t
                        break
                if c!=None:
                    for state in self.subsequences[c]:

                        peaks.append(tuple([self.orderedDateList[int(state)], 1.0, deepcopy(transform)]))
        return peaks

    def read(self, filez, timing='relative'):
        if not os.path.isfile(filez):
            print "Give a valid file!!"
            return False
        with open(filez, 'r') as jfile:
            self.reset()
            data = json.load(jfile)
        self.available = False
        self.typeID = data['typeID']
        if self.typeID=="MIDI":
            self.contents_type = Events.ClassicMIDIContents
        elif self.typeID=="Audio":
            self.contents_type = Events.ClassicAudioContents
        self.reset()
        for i in range(1, len(data['data'])):
            self.append(data['data'][i]['time'][timing][0], data['data'][i])
        self.available = True
        self.current_file = filez
        return True

    def change_ngram(self, ngram_size):
        try:
            self.ngram_size = int(ngram_size)
        except:
            print("[ERROR memorySpace] ngram size must be an integer")
        self.ngram_size = ngram_size
        self.build_subsequences()
        print("[INFO] ngram size of", self, "set to", ngram_size)


    def reset(self):
        self.buffer = deque([], self.ngram_size)
        self.subsequences = dict()
        self.orderedDateList = list()
        self.orderedEventList = list()
