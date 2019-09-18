{
  "typeID": str,
  "size": i,
  "type": i,
  "name": str,
  "data": [
    {
      "seg": [i, i],
      "state": i,
      "slice": [i, i],
      "beat": [f, f, i, i],
      "time": [i, f],
      "notes": [
          {
              "note": [i, i, i]
              "time": [f, f]
          }
      ],
      "extras": [f x 12],
    }
  ]
}


##########
# Head   #
##########

"typeID": Name of format
    typeID := "MIDI" | "Audio"

"size": Number of states in data dict

"type": Don't know. Set to 3 in all cases in the code

"name": Name of corpus

"data": List of dicts containing all the content of the file, see below

###########
# Content #
###########
Each item of the list "data" contains a dictionary representing a single state, which may contain zero, one or multiple notes.

"seg": Don't know. Always [1, 0]

"state": Index of current state (in [0, size-1])

"slice": Consists of two numbers:
    0. Represents fundamental, virtual fundamental or no fundamental: 0-127 represents midi pitches, 128-139 virtual fundamentals (0-11) and 140 represents no fundamental
    1. Don't know. is always 0.0

"beat": Consists of four numbers:
    0. Absolute beat as decimal (ex. 1.5 is middle of second beat)
    1. Tempo in BPM
    2. Don't know. is always 0.0
    3. Don't know. is always 0.0

"time": Consists of two numbers:
    0. Absolute position of state beginning in ms
    1. Tempo in BPM                                      <!-- is this is  -->

"notes": List of dicts, where each dict contains two entries:
    "note": [nn, vel, ch],
    "time": Not sure.

"extras": Twelve floats representing chroma


