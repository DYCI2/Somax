
from CorpusBuilder import CorpusBuilder
from ops import OpSomaxMelodic

corpus_path = "./examples/debussy.mid"
# we build the CorpusBuilder object with the path of the corpus
builder = CorpusBuilder(corpus_path)



standardOp = builder.ops[''][0]
print builder.ops

# setting the foreground channels as in the interactive mode

standardOp.fgChannels = [2,3,4]
standardOp.bgChannels = [1,2,3,4]



#adding an operation to the standard built one
MelOp = OpSomaxMelodic(standardOp.file_paths, standardOp.corpus_name)
MelOp.fgChannels = [1]
builder.ops['m']= (MelOp, builder.ops[''][1])

print builder.ops

builder.build_corpus("./examples/output/")
