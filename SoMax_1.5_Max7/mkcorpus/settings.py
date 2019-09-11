import os

#######################
# Default settings    #
#######################

DEFAULT_CORPUS_PATH = os.getcwd()
CORPUS_FOLDER_NAME = 'corpus'
DEFAULT_FOREGROUND = list(range(1, 17))
DEFAULT_SELF_BACKGROUND = list(range(1, 17))
DEFAULT_MEL_BACKGROUND = [1]
DEFAULT_HARM_BACKGROUND = list(range(1, 17))

AUDIO_EXTENSIONS = ['.wav', '.aif', '.aiff']
MIDI_EXTENSIONS = ['.mid', '.midi']
ADMITTED_EXTENSIONS = AUDIO_EXTENSIONS + MIDI_EXTENSIONS

#######################
# File extension keys #
#######################

STANDARD_FILE_EXT = ''
MELODIC_FILE_EXT = 'm'
HARMONIC_FILE_EXT = 'h'

#######################
# Logs                #
#######################

MAIN_LOGGER = 'main_log'
DEBUG_INDENT = ' ' * 9
CRITICAL_INDENT = ' ' * 12
INFO_INDENT = ' ' * 8

#######################
# Other               #
#######################

# Set this to write the raw midi file as a note matrix for debugging purposes.
#     See docstring of `OpSomaxStanadard.readMIDIFiles for formatting.
WRITE_NOTE_MATRIX = False
