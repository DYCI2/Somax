
from CorpusBuilder import CorpusBuilder
from ops import OpSomaxMelodic

corpus_path = "./examples/keith.mid"

builder = CorpusBuilder(corpus_path, corpus_name="keith_rh")
print builder.ops
standardOp = builder.ops[''][0]
standardOp.fgChannels = [1]
standardOp.bgChannels = [2]
MelOp = OpSomaxMelodic(standardOp.file_paths, standardOp.corpus_name)
MelOp.fgChannels = [1]
builder.ops['m']= (MelOp, builder.ops[''][1])
builder.build_corpus("./examples/output/")


corpus_path = "./examples/keith.mid"

builder = CorpusBuilder(corpus_path, corpus_name="keith_lh")
standardOp = builder.ops[''][0]
standardOp.fgChannels = [2]
standardOp.bgChannels = [1]
MelOp = OpSomaxMelodic(standardOp.file_paths, standardOp.corpus_name)
MelOp.fgChannels = [1]
builder.ops['m']= (MelOp, builder.ops[''][1])

builder.build_corpus("./examples/output/")
