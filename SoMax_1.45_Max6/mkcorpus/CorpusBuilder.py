import tools, virfun, json
from numpy import asarray
from string import split, join
import sys,os, re, importlib, shutil

class CorpusBuilder(): # main class to instantiate to achieve corpus construction.
                       # Initializes with a path to the files and a corpus name.
    verbose = 0
    def __init__(self, corpus_path, corpus_name = None,  **kwargs):
        if 'verbose' in kwargs.keys():
            self.verbose = kwargs["verbose"]
        else:
            self.verbose = False

        if 'callback_dic' in kwargs.keys():
            self.callback_dic = kwargs["callback_dic"]
        else:
            self.callback_dic = {'': 'OpSomaxStandard', 'h': 'OpSomaxHarmonic', 'm': 'OpSomaxMelodic'}

        self.corpus_path=str(corpus_path)
        if corpus_name==None:
            self.corpus_name = os.path.splitext(os.path.basename(corpus_path))[0] # without explicit corpus name, take the name of the corpus path
        else:
            self.corpus_name = corpus_name


        if self.verbose:
            print ""
            print "Corpus name set to :", self.corpus_name

        self.ops = dict()

        # the CorpusBuilder, at initialization, builds a proposition for the operations to be made.
        # the operation dictionary is a dictionary labelled by suffix containing the files to be analyzed.
        # the operation corresponding to a given suffix will be so executed to whole of the files.
        if os.path.isfile(corpus_path):
            self.ops_index = self.ext_files_from(self.corpus_path) # if a file, scan the current folder to get the files
        elif os.path.isdir(corpus_path):
            os.path.walk(corpus_path, lambda a,d,n: self.browse_folder(a,d,n), corpus_path) # if a folder, scan the given folder with files in it
        else:
            raise Exception("The corpus file(s) have not been found!!")

        for ids, names in self.ops_index.iteritems():
            Op = getattr(importlib.import_module("ops"), self.callback_dic[ids])
            operation = Op(names, self.corpus_name)
            self.ops[ids] = (operation, names)

        if self.verbose:
            self.print_ops()

    # triggers the corpus computation. This is made in two phases to let the user modify the operations if needed.
    def build_corpus(self, output_folder="./../corpus/"):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for ids, names in self.ops.iteritems():
            if ids!='':
                output_file = output_folder+self.corpus_name+'_'+ids+'.json'
            else:
                output_file = output_folder+self.corpus_name+'.json'
            for i in names[1]:
                if not os.path.splitext(i)[-1] in names[0].admitted_extensions:
                    raise Exception("File "+i+" not understood by operation ", callback_dic[ids])
            names[0].process(output_file)
            for item in names[1]:
                shutil.copyfile(item, output_folder+"/"+self.corpus_name)

    def print_ops(self):
        print ""
        print "Operations deduced : "
        for k,v in self.ops.iteritems():
            e = str(k)
            if e=='':
                e='main : '
            else:
                e = e + ' extension : '
            print e, self.callback_dic[k], "operation for", v[1]
        print ""

    def browse_folder(self, corpus_path, dirname, names): # function called to build the operation dictionary on every file of a folder.
        names = filter(lambda x: x[0]!='.', names) # exclude hidden files
        file_dict = dict()
        Op = getattr(importlib.import_module("ops"), self.callback_dic[''])

        main_files = filter(lambda x: len(x.split('_'))==1 and os.path.splitext(x)[1] in Op.admitted_extensions, names)
        file_dict[''] = map(lambda x: dirname+'/'+x, main_files)
        # looking
        potential_files = filter(lambda x: "".join(x.split('_')[:-1]) in map(lambda x : os.path.splitext(x)[0], main_files), names)
        for f in potential_files:
            suffix = os.path.splitext(f)[0].split('_')[-1]
            try:
                file_dict[suffix].append(dirname+'/'+f)
            except KeyError:
                file_dict[suffix] = [dirname+'/'+f]

        # gerer ca!!!
        for k,v in file_dict.iteritems():
            if k!='':
                if len(v)<len(file_dict[""]):
                    print "missing object"
                elif len(v)>len(file_dict[""]):
                    print "too many object"

        self.ops_index = file_dict


    def ext_files_from(self, corpus_path):
        full_path = os.path.realpath(corpus_path)
        dir_name = "/".join(full_path.split('/')[0:-1])
        corpus_name = os.path.splitext(os.path.basename(corpus_path))[0]
        files = os.listdir(dir_name)
        file_dict=dict()
        for f in files:
            name, ext = os.path.splitext(f)
            parts = split(name,'_')
            if parts[0]==corpus_name:
                if len(parts)==1:
                    Op = getattr(importlib.import_module("ops"), self.callback_dic[''])
                    if ext in Op.admitted_extensions:
                        file_dict[''] = [dir_name+'/'+f]
                else:
                    Op = getattr(importlib.import_module("ops"), self.callback_dic[parts[-1]])
                    if ext in Op.admitted_extensions:
                        file_dict[parts[-1]] = [dir_name+'/'+f]
        if self.verbose:
            print ""
            print "relevent files found : "
            print file_dict
        return file_dict
