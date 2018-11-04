import Events
from numpy import roll
from copy import deepcopy

# abstract class that represents identity, only if the class of the object
#       is in the transformation catalog

class NoTransform(object):
    def __init__(self):
        self.admitted_types = [Events.AbstractLabel, Events.AbstractContents] # dictionary of admitted label classes

    def __repr__(self):
        return "No Transformation"

    def __desc__(self):
        return 'NoTransformation'

    def encode(self, thing):
        return thing

    def decode(self, thing):
        return thing

    def __eq__(self, a):
        if type(a)==type(self):
            return True
        else:
            return False

    @classmethod
    def get_transformation_patterns(cls):
        return [cls()]


# obligatoirement mod12?
class TransposeTransform(NoTransform):
    transposition_range = [-3, 3]
    def __init__(self, semitone, mod12 = True):
        self.semitone = semitone
        self.mod12 = True
        self.admitted_types = [Events.MelodicLabel, Events.HarmonicLabel, Events.ClassicMIDIContents, Events.ClassicAudioContents]

    def __repr__(self):
        return "Transposition of "+str(self.semitone)+" semi-tones"

    def __desc__(self):
        return 'TransposeTransform'

    def encode(self, thing):
        if isinstance(thing, Events.AbstractEvent):
            new_thing = deepcopy(thing)
            new_thing.label = self.encode(new_thing.label)
            new_thing.contents = self.encode(new_thing.contents)
            return new_thing
        if type(thing) is Events.MelodicLabel:
            new_label = deepcopy(thing)
            new_label.label+=self.semitone # pas precis : rajouter les bornes et les accords
            return new_label
        elif type(thing) is Events.HarmonicLabel:
            chromas = list(thing.chroma)
            new_label = Events.HarmonicLabel(roll(thing.chroma, self.semitone))
        elif type(thing) is Events.ClassicMIDIContents:
            new_content = deepcopy(thing)
            for u in new_content.contents["notes"]:
                u["pitch"]+=float(self.semitone)
            return new_content
        elif type(thing) is Events.ClassicAudioContents:
            new_content = deepcopy(thing)
            new_content.transpose+=float(self.semitone*100.0)
            return new_content
        else:
            raise TransformError(thing, self)

    def decode(self, thing):
        if isinstance(thing, Events.AbstractEvent):
            new_thing = deepcopy(thing)
            new_thing.label = self.decode(new_thing.label)
            new_thing.contents = self.decode(new_thing.contents)
            return new_thing
        if type(thing) is Events.MelodicLabel:
            new_label = deepcopy(thing)
            new_label.label-=self.semitone # pas precis : rajouter les bornes et les accords
            return new_label
        elif type(thing) is Events.HarmonicLabel:
            chromas = list(thing.chroma)
            new_label = Events.HarmonicLabel(roll(thing.chroma, -self.semitone))
        elif type(thing) is Events.ClassicMIDIContents:
            new_content = deepcopy(thing)
            for u in new_content.contents["notes"]:
                u["pitch"]-=float(self.semitone)
            return new_content
        elif type(thing) is Events.ClassicAudioContents:
            new_content = deepcopy(thing)
            new_content.transpose-=float(self.semitone*100)
            return new_content
        else:
            raise TransformError(thing, self)

    def __eq__(self, a):
        if type(a)==NoTransform and self.semitone==0:
            return True
        elif type(a)==TransposeTransform:
            if self.mod12 and a.mod12:
                return self.semitone%12==a.semitone%12
            else:
                return self.semitone==self.semitone
        else:
            return False

    @classmethod
    def get_transformation_patterns(cls, r=None):
        r = r if r!=None else TransposeTransform.transposition_range
        transforms = []
        for s in range(r[0], r[1]+1):
            transforms.append(cls(s))
        return transforms

    @classmethod
    def set_transformation_range(cls, minim, maxim):
        cls.transposition_range = [minim, maxim]
        print "[INFO] Default transposition range set to",cls.transposition_range

class TransformError(Exception):
    def __init__(self, thing, transform):
        self.thing = thing
        self.transform = transform
    def __str__(self):
        return "Couldn't apply "+str(type(self.transform))+" on object "+str(type(self.thing))
