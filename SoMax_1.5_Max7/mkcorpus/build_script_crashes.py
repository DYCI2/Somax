

from CorpusBuilder import CorpusBuilder

corpus_path = "./examples/debussy"
# we build the CorpusBuilder object with the path of the corpus
builder = CorpusBuilder(corpus_path)

print builder.ops

builder.build_corpus("./examples/output/")
