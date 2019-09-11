from string import split
import sys, os, importlib
import logging, settings
from ops import OpSomaxStandard, OpSomaxHarmonic, OpSomaxMelodic


class CorpusBuilder:
    """ Main class to instantiate to achieve corpus construction. """

    def __init__(self, input_path, foreground_channels=None, self_bg_channels=None, mel_bg_channels=None,
                 harm_bg_channels=None, corpus_name=None, uses_legacy_parser=False, **kwargs):
        """ Generates a list of files and operations (legacy: based on existing files in corpus path) required for
            building the corpus but does not create the actual files."""

        self.logger = logging.getLogger(settings.MAIN_LOGGER)
        if 'callback_dic' in kwargs.keys():
            self.callback_dic = kwargs["callback_dic"]
        else:
            self.callback_dic = {'': 'OpSomaxStandard', 'h': 'OpSomaxHarmonic', 'm': 'OpSomaxMelodic'}

        self.input_path = str(input_path)
        if corpus_name is None:
            # without explicit corpus name, take the name of the corpus path
            self.corpus_name = os.path.splitext(os.path.basename(input_path))[0]
        else:
            self.corpus_name = corpus_name

        self.logger.debug('Corpus name set to {}'.format(self.corpus_name))

        # TODO: Clean up! This could be simplified a lot!
        #       If the very ugly lambda expression in generate_ops can be removed, ops_filepaths does not have
        #       to be global. then self.generate_ops could return ops, i.e. self.ops = self.generate_ops().
        self.ops = dict()  # type: {str: (MetaOp, [str])}
        self.ops_filepaths = dict()  # type: {str: [str]}

        self.generate_ops(input_path, foreground_channels, self_bg_channels, mel_bg_channels, harm_bg_channels,
                          uses_legacy_parser)
        # self.debug_print_ops()

    def generate_ops(self, input_path, foreground_channels, self_bg_channels, mel_bg_channels, harm_bg_channels,
                     uses_legacy_parser):
        """Generates the dict containing the corresponding `MetaOp`s.

           Always adds OpSomaxStandard, OpSomaxMelodic and OpSomaxHarmonic.
           If legacy flag: Will check the folder for separate files with names _h.mid or _m.mid, if either of
                            those exist, OpSomaxHarmonic and/or OpSomaxMelodic will be generated with these as input
                            files.
           If legacy flag is not set or the above mentioned files do not exist: the default midi file will be used to
           generate these

           (Old docstring: the CorpusBuilder, at initialization, builds a proposition for the operations to be made.
                           the operation dictionary is a dictionary labelled by suffix containing the files to be
                           analyzed. the operation corresponding to a given suffix will be so executed to whole of the
                           files.)
        """
        if os.path.isfile(input_path):
            # if input is a file and legacy flag is set, scan the current folder to get the files
            if uses_legacy_parser:
                self.ops_filepaths = self.get_linked_files_legacy(self.input_path)
            # otherwise create dictionary with same formatting as legacy parser, containing only the main item
            else:
                self.ops_filepaths = {settings.STANDARD_FILE_EXT: [input_path]}
        elif os.path.isdir(input_path):
            # if a folder, scan the given folder with files in it
            os.path.walk(input_path, lambda a, d, n: self.store_filepaths(a, d, n, uses_legacy_parser), input_path)
        else:
            # Note! This error has most likely been caught eariler, but will be kept just in case.
            self.logger.critical("The corpus file(s) were not found! Terminating script without output.")
            sys.exit(1)

        # Dynamic Generation of SomaxOp objects
        for key, filepaths in self.ops_filepaths.iteritems():
            op_class = getattr(importlib.import_module("ops"), self.callback_dic[key])
            op_object = op_class(filepaths, self.corpus_name)
            self.ops[key] = op_object
            self.logger.debug("Added operator {0} related to file(s) {1}".format(self.callback_dic[key], filepaths))

        # Adding harmonic and melodic output files if no matching midi files are found
        if settings.MELODIC_FILE_EXT not in self.ops.keys():
            standard_filepaths = self.ops[settings.STANDARD_FILE_EXT].getFilePaths()
            if self.all_files_are_midi(standard_filepaths):
                self.ops[settings.MELODIC_FILE_EXT] = OpSomaxMelodic(standard_filepaths, self.corpus_name)
                self.logger.debug("No _m file found. Added Melodic operator based on standard file(s) ({0})."
                                  .format(standard_filepaths))
        if settings.HARMONIC_FILE_EXT not in self.ops.keys():
            standard_filepaths = self.ops[settings.STANDARD_FILE_EXT].getFilePaths()
            self.ops[settings.HARMONIC_FILE_EXT] = OpSomaxHarmonic(standard_filepaths, self.corpus_name)
            self.logger.debug("No _h file found. Added Harmonic operator based on based on standard file(s) ({0})."
                              .format(standard_filepaths))

        # Setting the channel values for each operator according to input specification
        for key, op in self.ops.iteritems():
            self.set_channels(op, key, foreground_channels, self_bg_channels, mel_bg_channels, harm_bg_channels)

    def set_channels(self, op_object, key, foreground_channels, self_bg_channels, mel_bg_channels, harm_bg_channels):
        op_object.setFgChannels(foreground_channels)
        if key == settings.STANDARD_FILE_EXT:
            op_object.setBgChannels(self_bg_channels)
        if key == settings.MELODIC_FILE_EXT:
            op_object.setBgChannels(mel_bg_channels)
        if key == settings.HARMONIC_FILE_EXT:
            op_object.setBgChannels(harm_bg_channels)

    def build_corpus(self, output_folder):
        output_files = []
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for key, op in self.ops.iteritems():
            if key != settings.STANDARD_FILE_EXT:
                output_file = output_folder + self.corpus_name + '_' + key + '.json'
            else:
                output_file = output_folder + self.corpus_name + '.json'
            for path in op.getFilePaths():
                if not os.path.splitext(path)[-1] in op.admitted_extensions:
                    self.logger.critical("File {0} is not understood by operation {1}. This should not have occurred."
                                         "Script terminating without output.".format(path, self.callback_dic[key]))
            # Run the actual operator
            op.process(output_file)
            output_files.append(output_file)
        return output_files

    def store_filepaths(self, corpus_path, dirname, names, uses_legacy_parser):
        """function called to build the operation dictionary on every file of a folder."""
        names = filter(lambda x: x[0] != '.', names)  # exclude hidden files
        file_dict = dict()
        Op = getattr(importlib.import_module("ops"), self.callback_dic[''])

        if uses_legacy_parser:
            main_files = filter(lambda x: len(x.split('_')) == 1 and os.path.splitext(x)[1] in Op.admitted_extensions,
                                names)
        else:
            main_files = filter(lambda x: os.path.splitext(x)[1] in Op.admitted_extensions, names)
        file_dict[''] = map(lambda x: dirname + '/' + x, main_files)
        # looking
        potential_files = filter(
            lambda x: "".join(x.split('_')[:-1]) in map(lambda x: os.path.splitext(x)[0], main_files), names)
        for f in potential_files:
            suffix = os.path.splitext(f)[0].split('_')[-1]
            try:
                file_dict[suffix].append(dirname + '/' + f)
            except KeyError:
                file_dict[suffix] = [dirname + '/' + f]

        # gerer ca!!!
        for k, v in file_dict.iteritems():
            if k != '':
                if len(v) < len(file_dict[""]):
                    print "missing object"
                elif len(v) > len(file_dict[""]):
                    print "too many object"

        self.ops_filepaths = file_dict

    def get_linked_files_legacy(self, input_file):
        dir_name = os.path.dirname(input_file) + '/'
        corpus_name = os.path.splitext(os.path.basename(input_file))[0]
        if '_' in corpus_name:
            self.logger.critical('Invalid name provided for corpus: the midi file must not contain underscores (_). \n'
                                 + settings.CRITICAL_INDENT +
                                 'Note that script should never be run on _h.mid or _m.mid files: these will\n'
                                 + settings.CRITICAL_INDENT +
                                 'automatically be loaded when running the script on the .mid file.\n'
                                 + settings.CRITICAL_INDENT +
                                 'Terminating the script without output.')
            sys.exit(1)

        files = os.listdir(dir_name)
        file_dict = dict()
        for f in files:
            name, ext = os.path.splitext(f)
            parts = split(name, '_')
            if parts[0] == corpus_name:
                if len(parts) == 1:
                    Op = getattr(importlib.import_module("ops"), self.callback_dic[''])
                    if ext in Op.admitted_extensions:
                        file_dict[''] = [dir_name + f]
                else:
                    Op = getattr(importlib.import_module("ops"), self.callback_dic[parts[-1]])
                    if ext in Op.admitted_extensions:
                        file_dict[parts[-1]] = [dir_name + f]
        self.logger.debug("Relevant files found: {}".format(file_dict))
        return file_dict

    def all_files_are_midi(self, filepaths):
        return all([os.path.splitext(p)[-1] in settings.MIDI_EXTENSIONS for p in filepaths])
