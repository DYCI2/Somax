
from CorpusBuilder import CorpusBuilder
from ops import OpSomaxMelodic, OpSomaxHarmonic

corpus_path = "./examples/debussy.mid"
# we build the CorpusBuilder object with the path of the corpus
builder = CorpusBuilder(corpus_path)



standardOp = builder.ops[''][0]
print builder.ops

# setting the foreground channels as in the interactive mode

standardOp.fgChannels = [2,3,4]
standardOp.bgChannels = [1,2,3,4]



#adding an operation to the standard built one
# MelOp = OpSomaxMelodic(standardOp.file_paths, standardOp.corpus_name)
# MelOp.fgChannels = [1]
# builder.ops['m']= (MelOp, builder.ops[''][1])

# print "1: ", standardOp.file_paths
# print "2: ", standardOp.corpus_name
# print "3: ", builder.ops[''][1]

# HarmOp = OpSomaxHarmonic(standardOp.file_paths, standardOp.corpus_name)
# HarmOp.fgChannels = [1]
# builder.ops['h']= (HarmOp, builder.ops[''][1])

print builder.ops

builder.build_corpus("./examples/output/")
