from Tools import SequencedList
from copy import deepcopy
import numpy as np
import math

class AbstractMergeAction(object):
    def merge(self, pattern, memory_space=None):
        return pattern

class DistanceMergeAction(AbstractMergeAction):
    def __init__(self, t_width = 0.1, transform_merge_mode = 'OR'):
        self.t_width = t_width
        self.transform_merge_mode = transform_merge_mode # can 'AND' or 'OR'

    def merge(self, pattern):
        if len(pattern)==0:
            return pattern
        n = len(pattern)
        z, (v, t) = pattern[0]
        i = 1
        while i<len(pattern):
            zb, vb, tb = z,v,t
            z,(v,t) = pattern[i]
            if i>0 and abs(z-zb)<0.9*self.t_width:
                if t==tb:
                    del pattern[i]
                    pattern[i-1] = (zb*vb+z*v)/(v+vb), (v+vb, t)
                else:
                    if self.transform_merge_mode=='AND':
                        del pattern[i]
                        del pattern[i-1]
                        i-=1
                    else:
                        i+=1
            else:
                i+=1
        return pattern

class StateMergeAction(AbstractMergeAction):
    def __init__(self, memory_space, t_width = 0.1, transform_merge_mode = 'AND'):
        self.t_width = 0.1
        self.memory_space = memory_space
        self.transform_merge_mode = transform_merge_mode # can 'AND' or 'OR'

    def merge(self, pattern, memory_space=None, scheduler=None):
        #print ''
        #print '------BEGINNING MERGE-------'
        if len(pattern)==0 or memory_space==None:
            return deepcopy(pattern)
        merged_pattern = SequencedList()
        states_list = []
        current_index = -1
        for i in range(len(pattern)):
            #print 'looop ',i
            #print 'current_index : ', current_index
            z, (v, t) = pattern[i]
            #print 'pattern at ', i, ' : ', z, v, t
            state, distance = self.memory_space.get_events(z)
            state, distance = state[0], distance[0]
            #print 'current state and distance : ', state, distance
            if current_index==-1:
                #print 'init loop'
                za, (va, ta) = pattern[i]
                merged_pattern.append(float(za), (float(va),deepcopy(ta)))
                states_list.append(state.index)
                current_index += 1
                #print 'merged pattern : ', merged_pattern
                continue

            if state==None:
                #print 'no state....'
                continue

            if state.index==states_list[current_index]:
                #print 'conflicting states found'
                if t == merged_pattern[current_index][1][1]:
                    #print "same transformations found"
                    za, (va, ta) = merged_pattern[current_index]
                    #print 'previous merged_pattern state : '; za, ta, va
                    za = (za*va+z*v)/(v+va)
                    va = v+va
                    #print 'updating to ', za, ' and value ', va, 'and trasform ', ta
                    merged_pattern[current_index] = za,(va,ta)
                    #print 'new merged patter at', current_index, ' : ', merged_pattern[current_index]
                else:
                    #print "different transformations"
                    za, (va, ta) = merged_pattern[current_index]
                    #print 'current merged pattern at ',current_index, ' : ', merged_pattern[current_index]
                    za = (za*va+z*v)/(v+va)
                    va = v+va
                    #print 'before conversion', ta
                    if type(ta)!=list:
                        ta = [ta]
                    #print 'after conversion', ta
                    cop = deepcopy(pattern[i][1][1])
                    #print 'original pattern : ', pattern[i][1][1]
                    #print 'copy of original pattern : ', pattern[i][1][1]
                    ta = ta + [cop]
                    #print 'after mutation : ', ta
                    #print 'updating to ', za, ' with transofrom ', va, ' and ta ', ta
                    merged_pattern[current_index] = za,(va,ta)
                    #print 'current merged pattern at ',current_index, ' : ', merged_pattern[current_index]
            else:
                #print 'different states'
                za, (va, ta) = pattern[i]
                merged_pattern.append(float(za), (float(va),deepcopy(ta)))
                states_list.append(state.index)
                #print 'appending ', state.index, ' to state list'
                current_index += 1
                #print 'current merged pattern at ',current_index, ' : ', merged_pattern[current_index]
        return merged_pattern

class PhaseModulationMergeAction(AbstractMergeAction):
    def __init__(self, scheduler, selectivity = 1.0):
        self.scheduler = scheduler
        self.selectivity = selectivity

    def merge(self, pattern, memory_space=None):
        current_time = self.scheduler.get_time()
        for i in range(0, len(pattern)):
            z, (v,t) = pattern[i]
            factor = math.exp(self.selectivity*(math.cos(2*math.pi*(current_time-z))-1))
            pattern[i] = z, (v*factor, t)
        return pattern

    def set_selectivity(self, selectivity):
        try:
            self.selectivity = float(selectivity)
        except:
            print("[ERROR] Phase modulation selectivity must be a number")
            pass
