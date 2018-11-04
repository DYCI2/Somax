import time, bisect
from Tools import SequencedList


###############################################################################
# SomaxScheduler is the global scheduler in SoMax.
# the main process is the set_time function, which updates the scheduler and
# gets back the events to handle.
#  the scheduler has a timeline, which is a sequenced list.


class SomaxScheduler(object):

    def __init__(self, automode=True, timing_type="relative", original_tempo = False):
        self.time = 0.0
        self.timeline = SequencedList()
        self.timescale = 1.0
        self.midi_queues = {}
        self.tempo = 120.0
        self.pretime = 0.1 # in seconds
        self.original_tempo = original_tempo
        self.triggers = dict() # list of triggering mode of every players
        self.timing_type = timing_type


    ######################################################
    ###### TIMING METHODS

    # starting the scheduler
    def start(self, time):
        self.reset()
        self.time = time - self.get_pretime()

    # stopping the scheduler
    def stop(self):
        self.reset()

    # setting time of the scheduler ; returns events to handle
    def set_time(self, time):
        self.time = time
        events = self.pop_events(time)
        return events

    # time accesors for players and server
    def get_time(self):
        return self.time



    ######################################################
    ###### WRITING METHODS

    # writing general data in the scheduler queue
    def write(self, player, time, *args): # writes events in scheduler
        self.timeline.insert(time, tuple([player])+args)

    # writing an event object in the queue
    def write_event(self, time, player, event, automode=True):
        if not event:
            return
        factor = self.tempo if self.timing_type=="relative" else self.timescale

        content_object = event.get_contents()
        contents = content_object.get_contents(self.timing_type, factor)
        trig_mode = self.triggers[player]
        midiCheck = False

        if trig_mode=="automatic":
            next_time = time+content_object.get_state_length(self.timing_type, factor)
            self.write('server', next_time-self.get_pretime(), "ask_for_event", player, next_time)
            midiCheck = True

        tempos = []
        if self.original_tempo:
            self.set_tempo(content_object.get_tempo())

        if trig_mode=="reactive" and player in self.midi_queues:
            elts = self.midi_queues[player].new_slice(trig_mode)
            for elt in elts:
                self.write(player, time+content_object.get_state_length(self.timing_type, factor), elt['content'])

        for elt in contents:
            if elt['content'][0]=='midi':
                if not player in self.midi_queues:
                    self.midi_queues[player] = MIDIQueue()
                elt = self.midi_queues[player].process_midi_event(elt, trig_mode)
                if elt!=None:
                    time_elt = time + elt['time'][0]
                    tempos.append(float(elt['time'][2]))
                    self.write(player, time_elt, elt['content'])
            else:
                time_elt = time + elt['time'][0]
                event_tempo = elt['time'][2]
                self.write(player, time_elt, elt['content'])
                '''if self.originalTempo and tempo!=None:
                    self.write(3, time, "set_tempo "+str(tempo))'''
        if midiCheck == True:
            elts = self.midi_queues[player].new_slice(trig_mode)
            for elt in elts:
                self.write(player, time+content_object.get_state_length(self.timing_type, factor), elt['content'])
        # if self.triggers[player]=="automatic":
        #     print "writing event at [2]", time, "next planned event : ", content_object.get_state_length(self.timing_type, factor)

    def pop_events(self, time):
        def opgklm(x):
            if x[0]=='internal':
                self.process_internal_event(x[1:])
                return False
            else:
                return True
        toplay, self.timeline = self.timeline.truncate(time)
        events_to_outlet = toplay.get_events_list()
        return filter(opgklm, events_to_outlet)

    def process_internal_event(self, event):
        if event[0]=="ask_for_event":
            self.ask_for_event(self.time+self.pre_time)
        if event[0]=="print":
            if len(event)>2:
                print event[2:]

    # external methods
    def set_original_tempo(self, original_tempo):
        self.original_tempo = original_tempo

    def set_tempo(self,tempo):
        self.tempo = tempo

    def set_timescale(self, timescale):
        self.timescale = timescale

    def reset(self, players=None):
        if players==None:
            self.timeline = SequencedList()
        else:
            if type(players)!=list:
                players = [players]
            for i in range(0, len(self.timeline)):
                t, c = self.timeline[i]
                if c[0] in players:
                    del self.timeline[i]
                    i -= 1
                elif c[0]=="server" and c[2] in players:
                    del self.timeline[i]
                    i -= 1

    def get_pretime(self, timing_type=None):
        timing_type = self.timing_type if timing_type==None else timing_type
        if timing_type == 'relative':
            # print round(self.pretime*(self.tempo/60)*10)/10
            return round(self.pretime*(self.tempo/60)*10)/10
        else:
            return self.pretime




###########################################################
###### MIDI queuing object to handle OMAX sliced midi data
class MIDIQueue(object):
    def __init__(self):
        self.tobeheld_notes = list()
        self.held_notes = list()

    def process_midi_event(self, event, triggering_mode="automatic"):
        midi, pitch, velocity, duration = event['content']
        offset, duration ,tempo = event['time']
        event_to_output = None
        if velocity>0 and duration>0:
            if triggering_mode == "reactive":
                duration = 1000
            self.held_notes.append(pitch)
            event_to_output = {"time":[offset, duration, tempo], "content":[midi, pitch, velocity, duration]}
        elif velocity==0:
            # normally, accumulate note offs
            if pitch in self.held_notes:
                i = self.held_notes.index(pitch)
                del self.held_notes[i]
                event_to_output = {"time":[offset, 0, tempo], "content":[midi, pitch, 0 ,duration]}
        elif offset<0:
            if not pitch in self.held_notes:
                event_to_output = {"time":[0, duration, tempo], "content":[midi, pitch, 80 ,duration]}
            self.tobeheld_notes.append(pitch)
        elif duration==0 and offset>=0:
            event_to_output = {"time":[offset, 1000, tempo], "content":[midi, pitch, velocity ,1000]}
            self.tobeheld_notes.append(pitch)
        return event_to_output

    def new_slice(self, trig_mode="automatic"):
        events = []
        for i in self.held_notes:
            events.append({"content":["midi", i, 0, 0]})
        self.held_notes = list(self.tobeheld_notes)
        self.tobeheld_notes = list()
        return events
