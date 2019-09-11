import os
import argparse
import logging
import settings
import ast
from CorpusBuilder import CorpusBuilder
from melodic_from_json import MelJsonGenerator


class Main:
    """ New build script. Designed without support for interactive mode"""

    def __init__(self, input_path, output_folder, is_verbose, foreground, self_bg, mel_bg, harm_bg, uses_mel_from_json,
                 uses_held_melodics, uses_legacy_parser):
        self.logger = Main.init_logger(is_verbose)

        if not os.path.isabs(input_path):
            input_path = os.path.normpath(os.getcwd() + '/' + input_path)

        self.logger.debug('Script was initialized with the following parameters:\n'
                          + settings.DEBUG_INDENT + 'Input file/folder: {0}\n'.format(input_path)
                          + settings.DEBUG_INDENT + 'Output folder: {0}\n'.format(output_folder)
                          + settings.DEBUG_INDENT + 'Foreground channel(s): {0}\n'.format(foreground)
                          + settings.DEBUG_INDENT + 'Self Background channel(s): {0}\n'.format(self_bg)
                          + settings.DEBUG_INDENT + 'Melodic Background channel(s): {0}\n'.format(mel_bg)
                          + settings.DEBUG_INDENT + 'Harmonic Background channel(s): {0}\n'.format(harm_bg))

        # NOTE! This primitive check will print a warning if the user is building the json file to a folder that is not
        #       named `corpus`. If the naming of the corpus folder will change in future versions,
        #       this check will be incorrect and must be corrected.
        if os.path.normpath(os.path.basename(output_folder)) != settings.CORPUS_FOLDER_NAME:
            self.logger.warn('Output folder is not set to default and will likely not be available inside SoMax, '
                             'is this intentional?\n'
                             'To ensure correct behaviour, please either run the script directly inside\n'
                             'the corpus folder of SoMax or use the -o option to point to this directory.')

        builder = CorpusBuilder(input_path, foreground_channels=foreground, self_bg_channels=self_bg,
                                mel_bg_channels=mel_bg, harm_bg_channels=harm_bg, uses_legacy_parser=uses_legacy_parser)

        # Build the corpus and write all the files (standard, harmonic and melodic)
        output_filepaths = builder.build_corpus(os.path.normpath(output_folder) + '/')
        log_string = "The following files were written:"
        for fp in output_filepaths:
            log_string += '\n' + settings.INFO_INDENT + fp
        self.logger.info(log_string)

        # Overwrite the generated melodic json file if flag is set
        if uses_mel_from_json:
            self.generate_mel_from_json(output_filepaths, uses_held_melodics)

    def generate_mel_from_json(self, output_filepaths, uses_held_melodics):
        """ Generates a melodic json file from the already generated standard json file.

        :param [str] output_filepaths: list of filepaths to json files
                                       (standard, harmonic, melodic and in that specific order).
        :param bool uses_held_melodics: see `MelJsonGenerator`
        """
        self.logger.debug('Writing melodic json using melodic_from_json with the following parameters:\n'
                          + settings.DEBUG_INDENT + 'Input file: {}\n'.format(output_filepaths[0])
                          + settings.DEBUG_INDENT + 'Held: {}\n'.format(uses_held_melodics))
        # Note that this assumes that the first file of `output_filepaths` always will be the standard json file.
        MelJsonGenerator.generate_mel_json(output_filepaths[0], uses_held_melodics)

    @staticmethod
    def path_if_valid(path):
        if os.path.exists(path):
            return path
        else:
            raise argparse.ArgumentTypeError('"{0}" is not a valid path'.format(path))

    @staticmethod
    def is_midi_audio_or_folder(path):
        Main.path_if_valid(path)
        _, file_ext = os.path.splitext(path)
        if file_ext in settings.ADMITTED_EXTENSIONS:
            return path
        elif os.path.isdir(path):
            return path
        else:
            raise argparse.ArgumentTypeError('"{0}" is not a midi file, audio file or a valid folder.'.format(path))

    @staticmethod
    def is_folder(path):
        Main.path_if_valid(path)
        if os.path.isdir(path):
            return path
        else:
            raise argparse.ArgumentTypeError('"{0}" is not a directory file.'.format(path))

    @staticmethod
    def init_logger(is_verbose):
        logger = logging.getLogger(settings.MAIN_LOGGER)
        ch = logging.StreamHandler()
        if is_verbose:
            logger.setLevel(logging.DEBUG)
            ch.setLevel(logging.DEBUG)  # Set output logging level, needs to be set twice (?)
        else:
            logger.setLevel(logging.INFO)
            ch.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(levelname)s]: %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    @staticmethod
    def parse_list(arg_name, list_as_string):
        try:
            # Note: a parser comma-separated list without spaces will be parsed as a tuple.
            maybe_list = ast.literal_eval(list_as_string)
            if isinstance(maybe_list, tuple) and all([isinstance(v, int) for v in maybe_list]):
                return list(maybe_list)
            elif isinstance(maybe_list, int):
                return [maybe_list]
            else:
                Main.throw_list_parse_error(arg_name, list_as_string)
        except (SyntaxError, ValueError) as e:
            Main.throw_list_parse_error(arg_name, list_as_string)

    @staticmethod
    def throw_list_parse_error(arg_name, list_as_string):
        raise argparse.ArgumentTypeError('Error while parsing "{0}": formatting should only be a list of '
                                         'integers without spaces.\n '
                                         'Example: 1,2,3,6\n'
                                         'Your input was: {1}.'.format(arg_name, list_as_string))

    @staticmethod
    def parse_fg(list_as_string):
        return Main.parse_list("Foreground", list_as_string)

    @staticmethod
    def parse_sbg(list_as_string):
        return Main.parse_list("Self Background", list_as_string)

    @staticmethod
    def parse_mbg(list_as_string):
        return Main.parse_list("Melodic Background", list_as_string)

    @staticmethod
    def parse_hbg(list_as_string):
        return Main.parse_list("Harmonic Background", list_as_string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",
                        help="Path to the midi file, audio file  or folder to parse (relative or absolute).",
                        type=Main.is_midi_audio_or_folder)
    parser.add_argument("-o", "--output_folder", help="Path to the corpus folder", type=Main.is_folder,
                        default=settings.DEFAULT_CORPUS_PATH)
    parser.add_argument("-v", "--verbose", help="Verbose output", action='store_true', default=False)
    parser.add_argument("-f", "--foreground",
                        help="When using a midi file as input, this argument specifies which midi channel(s) that will "
                             "be used as foreground (output) by Somax. Channels must be specified as a comma separated "
                             "list without spaces. \n"
                             "EXAMPLE: 1,2,8 will result in channels 1, 2 and 8 as output channels.",
                        type=Main.parse_fg, default=settings.DEFAULT_FOREGROUND)
    parser.add_argument("-s", "--self_bg",
                        help="When using a midi file as input, this argument specifies which midi channel(s) Somax "
                             "will listen to when mode is set to SELF. \n"
                             "Formatting: see --foreground",
                        type=Main.parse_sbg, default=settings.DEFAULT_SELF_BACKGROUND)
    parser.add_argument("-m", "--mel_bg",
                        help="When using a midi file as input, this argument specifies which midi channel(s) Somax "
                             "will listen to when mode is set to MELODIC. \n"
                             "Formatting: see --foreground",
                        type=Main.parse_mbg, default=settings.DEFAULT_MEL_BACKGROUND)
    parser.add_argument("-b", "--harm_bg",
                        help="When using a midi file as input, this argument specifies which midi channel(s) Somax "
                             "will listen to when mode is set to HARMONIC. \n"
                             "Formatting: see --foreground",
                        type=Main.parse_hbg, default=settings.DEFAULT_HARM_BACKGROUND)
    parser.add_argument("--melodic-from-json",
                        help="When using a midi file as input: if this flag is set, the script melodic_from_json "
                             "will be run to generate the melodic json file from the standard file. "
                             "Note that setting this flag will override any other setting defined for melodic content.",
                        action='store_true', default=False)
    parser.add_argument("--melodic-are-held",
                        help="Recommended flag for --melodic-from-json. If set, takes into account notes even if "
                             "they were played in a previous state.", action='store_true', default=False)
    parser.add_argument("--legacy",
                        help="Legacy support for separate _h.mid and _m.mid files. Setting this flag means that the"
                             "parser will scan the folder of the input file for separate midi files containing harmonic"
                             "and/or melodic information. Note that the legacy parser is very primitive and will"
                             "(among other things) not allow underscores in any filenames apart from the trailing"
                             "_h.mid and _m.mid.", action='store_true', default=False)

    args = parser.parse_args()

    Main(args.inputfile, args.output_folder, args.verbose, args.foreground, args.self_bg, args.mel_bg, args.harm_bg,
         args.melodic_from_json, args.melodic_are_held, args.legacy)
