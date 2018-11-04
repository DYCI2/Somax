import ActivityPatterns
import MemorySpaces
import StreamViews
import Tools
import Events
import SoMaxScheduler
import Players
import Transforms
import Atom
import MergeActions
import OSC
import GenCorpus
import CorpusBuilder

reload(ActivityPatterns)
reload(MemorySpaces)
reload(StreamViews)
reload(Tools)
reload(Events)
reload(SoMaxScheduler)
reload(Players)
reload(Transforms)
reload(Atom)
reload(MergeActions)


TRANSFORM_TYPES = [Transforms.NoTransform, Transforms.TransposeTransform]
LABEL_TYPES = [Events.MelodicLabel, Events.HarmonicLabel]
CONTENTS_TYPES = [Events.ClassicMIDIContents, Events.ClassicAudioContents]
EVENT_TYPES = [Events.AbstractEvent]
MEMORY_TYPES = [MemorySpaces.NGramMemorySpace]

'''reload(ActivityPatterns)
reload(MemorySpaces)
reload(StreamViews)
reload(Tools)
reload(Events)
reload(SoMaxScheduler)'''
