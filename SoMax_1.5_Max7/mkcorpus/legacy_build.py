import sys, os, re, importlib, inspect, logging, argparse
from CorpusBuilder import CorpusBuilder

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception("not enough arguments to the script!")
    elif len(sys.argv) == 2:
        corpus_path = sys.argv[1]
        builder = CorpusBuilder(corpus_path)
        builder.build_corpus("./")
    elif len(sys.argv) == 3:
        option = sys.argv[1]

        # interactive mode
        if option == "-i":
            corpus_path = sys.argv[2]
            builder = CorpusBuilder(corpus_path, verbose=True)
            print ""
            print "Do you want to modify an operation? (h for help)"
            cont = 1
            while cont:
                ans = raw_input("? ")
                if ans == '':
                    cont = 0
                elif ans == 'h':
                    print "type o to re-print all the operations"
                    print "type p <extension> to list the operation's paramaters of the given extension"
                    print "type r <extension> <op> to replace an operation for the given extension"
                    print "type s <extension> <parameter> <value> to change an operation parameter"
                    # print "type r <file> to remove a file in the corpus"
                elif ans == 'o':
                    builder.debug_print_ops()
                else:
                    p = ans.split()
                    if len(p) == 3 and p[0] == 'r':
                        if p[1] in builder.ops.keys():
                            try:
                                Op = getattr(importlib.import_module("ops"), p[2])
                                operation = Op(names, builder.corpus_name)
                                builder.ops[p[1]][0] = operation
                                print ""
                                print "New operations :"
                                print builder.debug_print_ops()
                            except:
                                print "not a valid operation!"
                                pass
                        else:
                            print "The extension has not been found!"

                    elif len(p) >= 4 and p[0] == 's':
                        if p[1] in builder.ops.keys():
                            res = builder.ops[p[1]][0].setParameter(p[2], p[3:])
                            if res != '':
                                print "ERROR:", res
                        else:
                            print "The extension has not been found!"
                    elif len(p) == 2 and p[0] == 'p':
                        if p[1] in builder.ops.keys():
                            builder.ops[p[1]][1].printParams()
                        else:
                            print "The extension has not been found!"

            cont = 1

            print "Where to output the file? (leave blank for default)"
            cont = 1
            while cont:
                out = raw_input("? ")
                if out == '':
                    out = "./../corpus/"
                    cont = 0
                elif os.path.exists(out):
                    cont = 0
                else:
                    print "the path doesn't exist!"
            builder.build_corpus(out)

        # verbose mode
        elif option == '-v':
            corpus_path = sys.argv[2]
            builder = CorpusBuilder(corpus_path, verbose=True)
            builder.build_corpus("./../corpus/")

        # output mode
        elif option == '-o':
            corpus_path = sys.argv[2]
            builder = CorpusBuilder(corpus_path)
            print "Where to output the file? (leave blank for default)"
            cont = 1
            while cont:
                out = raw_input("? ")
                if out == '':
                    out = "./../corpus/"
                    cont = 0
                elif os.path.exists(out):
                    cont = 0
                else:
                    print "the path doesn't exist!"
            builder.build_corpus(out)
