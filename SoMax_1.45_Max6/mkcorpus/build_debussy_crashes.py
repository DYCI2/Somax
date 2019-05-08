
from CorpusBuilder import CorpusBuilder
from ops import OpSomaxMelodic

corpus_path = "./debussy"
# we build the CorpusBuilder object with the path of the corpus
builder = CorpusBuilder(corpus_path)



StandardOp = builder.ops[''][0]
print builder.ops


# setting the foreground channels as in the interactive mode
#StandardOp.setParameter('fgChannels', '2 3 4')
#StandardOp.setParameter('bgChannels', '1 2 3 4')

# or directly into the attributes of the Op object
StandardOp.fgChannels = [2,3,4]
StandardOp.bgChannels = [1,2,3,4]

HarmOp = builder.ops['h'][0]
HarmOp.fgChannels = [1,2,3,4]
HarmOp.bgChannels = [1,2,3,4]

#adding an operation to the standard built one
MelOp = OpSomaxMelodic(StandardOp.file_paths, StandardOp.corpus_name)
MelOp.fgChannels = [1]
MelOp.bgChannels = [1,2,3,4]
builder.ops['m']= (MelOp, builder.ops[''][1])

print builder.ops

builder.build_corpus("./../corpus/")
