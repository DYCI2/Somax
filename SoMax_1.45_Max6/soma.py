#  -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:41:44 2013

@author: lbg
"""

import bisect
import json
import numpy as np




class ActivityPattern(): # compute the activity profile through time (cf time and partial sequence matching in the report)
                         # and by insertion of new events
    """memory activity structure"""
    tau_mem_decay = 2.0
    t_width = 0.1
    extinction_threshold = 0.1

    available = 1


    def __init__(self):
        self.date = 0.0 # absolute time elapsed
        self.zeta = np.array([]) # relative time elpased zeta = psi(t)
        self.value = np.array([]) # values of activity

    def update_activity(self, new_date): # updates the activity for the time translation
        if self.available:
            self.available = 0
            self.zeta += new_date - self.date
            self.value *= np.exp(-np.divide(new_date - self.date,
                                            self.tau_mem_decay))
            self.date = new_date
            self.clean_up()
            self.available = 1

    def clean_up(self): # erases from the memory places below the extinction threshold
        cond_tmp = self.value < self.extinction_threshold
        itmp = cond_tmp.nonzero()
        self.zeta = np.delete(self.zeta,itmp)
        self.value = np.delete(self.value,itmp)


    def insert(self, new_zeta_list, new_value_list): #inserts a new event in the activity pattern
        if self.available:
            self.available = 0
            zeta_tmp = self.zeta
            value_tmp = self.value
            z_tmp, v_tmp = merge(list(zeta_tmp), list(value_tmp),
                                 new_zeta_list, new_value_list)
            self.zeta = np.array(z_tmp)
            self.value = np.array(v_tmp)
            self.value = scale_activity(self.value)
            self.available = 1


    def get_activity(self): # returns the activity
        if self.available:
            self.available = 0
            ztmp = np.array(self.zeta)
            vtmp = np.array(self.value)

            self.available = 1
            return ztmp,vtmp
        else:
            print ' oooooooo not available in get activity oooooooo '
            return np.array([]), np.array([])




class KappaSpace():
    """knowledge space"""

    #dict ke_map: maps a location kappa_i with an ordered list of events zeta_i
    #kappa_activation : representation to kappa location

    # dictionary of small subsequences
    # a subseq (sseq) is a represented as a tuple
    ngram_size = 2
    location = ""

    def kappa_activation_pitch(self, pitch): # liste des fonctions d'activation pour chaque sous-type
        return pitch, 1.0


    def kappa_activation_som_mc(self, mel_contour):
        tmp = np.exp(-self.node_specificity*np.sqrt(np.sum(
                    self.weight*np.power(mel_contour-self.som,2), axis=1)))
        indtmp = np.argsort(tmp)
        return indtmp[-8:], tmp[indtmp[-8:]]

    def kappa_activation_som_chr(self, chroma):
        # normalize so that max is always 1.
        chroma = np.array(chroma)
        max_tmp = np.max(chroma)
        if max_tmp > 0.:
            chroma = chroma / np.max(chroma)
        tmp = np.exp(-self.node_specificity*np.sqrt(np.sum(
                np.power(chroma-self.som,2), axis=1)))
        indtmp = np.argsort(tmp)
        # this is tmp; 1.0 as categ, but true a_i should be used
        return self.som_c[indtmp[-1]], 1.0

    def map_kappa_to_events(self, event_list, rep_list, from_ind=0):
        for i in range(max(self.ngram_size-1, from_ind),len(event_list)):
            zeta_tmp = event_list[i]
            rep_tmp = tuple(rep_list[i+1-self.ngram_size:i+1])
            try:
                self.ke_map[rep_tmp].append(zeta_tmp) # ke-map est un dictionnaire donc les keywords sont les tuples!!
            except KeyError:
                self.ke_map[rep_tmp] = [zeta_tmp]

    def set_location(self, location):
        self.location = location
        filename = self.location + '/tables/'+'misc_hsom'
        self.som = np.loadtxt(str(filename),dtype=float,delimiter=',')
        filename = self.location + '/tables/'+'misc_hsom_c'
        self.som_c = np.loadtxt(str(filename),dtype=float,delimiter=',')

    def __init__(self, ktype, location=""):
        self.ke_map = {}
        self.location=location
        self.node_specificity = 2.0
        self.kappa_activity_threshold = 0.4
        if ktype == 'pitch':
            #0:128; #for now simply pitch 0-127; pc 128-139; rest 140
            self.kappa_activation = self.kappa_activation_pitch
        elif ktype == 'som_chroma':
            if self.location!="":
                filename = self.location + '/tables/'+'misc_hsom'
                self.som = np.loadtxt(str(filename),dtype=float,delimiter=',')
                filename = self.location + '/tables/'+'misc_hsom_c'
                self.som_c = np.loadtxt(str(filename),dtype=float,delimiter=',')
            self.kappa_activation = self.kappa_activation_som_chr
        # [...]
        else:
            print 'do not know this type of knowledge'


class StreamView():
    """a specific view of the musical stream"""
#    mm_data : mémoire chargée du .json
#
#    event_list = []

    def __init__(self, k_self, ngram_size=2):
        # the type of knowledge should be accessible from an outside param
        self.id = np.random.rand()
        self.k_self_listening = KappaSpace(k_self)
        self.k_self_listening.ngram_size = ngram_size
        if k_self == 'pitch':
            self.compute_pre_rep = self.compute_pre_rep_pitch
        elif k_self == 'som_melodic_contour':
            self.compute_pre_rep = self.compute_pre_rep_melc
        elif k_self == 'som_chroma':
            self.compute_pre_rep = self.compute_pre_rep_chroma
        self.reset()

    def reset(self):
        self.activity = ActivityPattern() # on supprime les activités précédentes
        self.mm_data = {}
        # initialize memory with empty silent slice
        self.mm_data['name'] = u'undefined name'
        self.mm_data['data'] = []
        self.mm_data['data'].append({u'slice': [140, 0], u'beat': [0.0, 0.0, 0, 0],
            u'notes': [], u'seg': [1, 0], u'state': 0,
            u'extras': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            u'time': [0, 0]})
        self.mm_data['size'] = 1 #TBR
        # for OMax compatibility; this is no longer needed
        # this is deprecated and will soon be removed
        self.mm_data['type'] = 3
        self.mm_data['typeID'] = u'MIDI'
        self.event_list = [0.0]
        self.rep_list = [140]
        self.event_history = [[0.0, 0]] #event 0 is silence
        self.kappa_event_history = []
        self.activation_threshold = 1.0
        self.self_listening_mod = 1.5
        self.taboo_mod = 0.2
        self.external_events = np.array([])
        self.eta_alpha = 0.001
        self.k_self_listening.ke_map = {}

    def load_mem(self,filename): # on charge la mémoire du .json et on initialise la stream view
        with open(filename+'.json', 'r') as json_file:
            self.reset()
            self.event_list = [] #TMP
            self.rep_list = []
            self.mm_data = json.load(json_file)
            # calls init stream_view
            self.init_stream_view()

    def init_stream_view(self):
        # create event list
        for i in range(len(self.mm_data['data'])): # pour chaque chunk de la mémoire chargée
            zeta_tmp = self.mm_data['data'][i]['beat'][0] # date de l'onset
            pre_rep_tmp = self.compute_pre_rep(i) # pré-réponse pour le chunk i
            rep_tmp, a_tmp = self.k_self_listening.kappa_activation(pre_rep_tmp) # on calcule l'activation selon le kappa-space
            self.event_list.append(zeta_tmp) # on rajoute la date de l'onset à la liste des zera
            self.rep_list.append(rep_tmp)         # on rajoute l'activation à la liste
        self.k_self_listening.map_kappa_to_events(self.event_list,
                                                  self.rep_list)

    def update_memory(self, new_slice):
        self.mm_data['data'].append(new_slice)
        self.mm_data['size'] += 1
        zeta_tmp = self.mm_data['data'][len(self.mm_data['data'])-1]['beat'][0]
        #pre_rep_tmp = self.compute_pre_rep(i)
        pre_rep_tmp = self.compute_pre_rep(len(self.mm_data['data'])-1)
        rep_tmp, a_tmp = self.k_self_listening.kappa_activation(pre_rep_tmp)
        self.event_list.append(zeta_tmp)
        self.rep_list.append(rep_tmp)
        self.k_self_listening.map_kappa_to_events(self.event_list,
                                                  self.rep_list, len(self.mm_data['data'])-1)


#    def compute_pre_rep_melc(self, event_trajectory):
#        melc_tmp = self.compute_melodic_contour(event_trajectory)
#        return melc_tmp

    # compute_pre_rep
    def compute_pre_rep_pitch(self, event):
        return self.mm_data['data'][event]['slice'][0]

    def compute_pre_rep_chroma(self, event):
        return self.mm_data['data'][event]['extras']


    def update_player_activity(self, new_date):
        self.activity.update_activity(new_date)
        # find zeta associated with kappa
        ke_sseq = []
        if len(self.kappa_event_history) >= self.k_self_listening.ngram_size:
            for k in range(self.k_self_listening.ngram_size):
                ke_sseq.insert(0, self.kappa_event_history[-(k+1)][1])
            ke_sseq = tuple(ke_sseq)
            try:
                zeta_tmp = np.array(self.k_self_listening.ke_map[ke_sseq])
                zeta_tmp = zeta_tmp + (new_date - self.kappa_event_history[-1][0])
                value_tmp = self.kappa_event_history[-1][2]*np.ones(zeta_tmp.size)
                #insert new zetas
                self.activity.insert(zeta_tmp, value_tmp)
            except KeyError:
                #print 'KeyError in update_player:: ie no corresponding zetas'
                pass


    def record_external_event(self, date):
        self.external_events = np.append(self.external_events,date)



class Player():

    verbose_mode = 1
    location = ""

    def __init__(self, k_s, s_ngram_size , k_m, m_ngram_size, k_h, h_ngram_size):
        # the type of knowledge should be accessible from an outside param
        # should a list of listeners
        # self listener

        # this is hardcoded for now
        # this will be easy to define and to adapt in the future
        self.s_l = StreamView(k_s, s_ngram_size)
        self.m_l = StreamView(k_m, m_ngram_size)
        self.h_l = StreamView(k_h, h_ngram_size)
        # weight
        self.s_w = 1.0/3.0
        self.m_w = 1.0/3.0
        self.h_w = 1.0/3.0

        self.prepare_to_jump = 0
        self.phase_ref = 0.

        self.phase_influence = 0
        self.gamma = 3
        self.adjust_phase = 0
        self.phase_adjustment_w = [0.1, 0.2]

        self.w_length = 8.0

        self.taboo_length = 8.0
        self.b_step = 1.0

        # for now assum taboo_dur=8. taboo_step=1.
        # tmp
        self.taboo_params = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

        # jumping parameters
        self.next_state = 1.0
        self.auto_jump_mode = 0
        self.tau_next_state = 1.0
        self.last_jump = 0.0

    def set_location(self, location):
        self.location = location
        self.s_l.k_self_listening.set_location(location)
        self.m_l.k_self_listening.set_location(location)
        self.h_l.k_self_listening.set_location(location)

    def load_mem(self,filename):
        filename_s = filename
        filename_m = filename+'_m'
        filename_h = filename+'_h'
        try:
           with open(filename_m+'.json'):
               pass
        except IOError:
           filename_m = filename
        try:
           with open(filename_h+'.json'):
               pass
        except IOError:
           filename_h = filename
        print filename_m
        self.s_l.load_mem(filename_s)
        self.m_l.load_mem(filename_m)
        self.h_l.load_mem(filename_h)

    def save_mem(self, name):
        with open(self.location+'/corpus/'+name+'.json', 'w') as new_json_file:
            json.dump(self.s_l.mm_data, new_json_file)
            print new_json_file, 'outputed'

    def new_event(self, date):
        self.new_event_histo = []
        # auto jump
        if self.auto_jump_mode:
            if (len(self.s_l.event_history) >= 2 and
                (self.s_l.event_history[-1][1]-1)
                != self.s_l.event_history[-2][1]):
                self.last_jump = self.s_l.event_history[-1][0]
            self.next_state = 8.15*np.exp(-(date-self.last_jump)/self.tau_next_state)

        ztmp_self, vtmp_self = self.s_l.activity.get_activity()
        # 'imagine' what the activity will look like
        ztmp_self += date - self.s_l.activity.date
        vtmp_self *= np.exp(-np.divide(date - self.s_l.activity.date,
                                       self.s_l.activity.tau_mem_decay))
        cond_tmp = vtmp_self < self.s_l.activity.extinction_threshold
        itmp = cond_tmp.nonzero()
        vtmp_self = np.delete(vtmp_self,itmp)
        ztmp_self = np.delete(ztmp_self,itmp)

        ztmp_mel, vtmp_mel = self.m_l.activity.get_activity()
        # 'imagine' what the activity will look like
        ztmp_mel += date - self.m_l.activity.date
        vtmp_mel *= np.exp(-np.divide(date - self.m_l.activity.date,
                                      self.m_l.activity.tau_mem_decay))
        cond_tmp = vtmp_mel < self.m_l.activity.extinction_threshold
        itmp = cond_tmp.nonzero()
        vtmp_mel = np.delete(vtmp_mel,itmp)
        ztmp_mel = np.delete(ztmp_mel,itmp)

        ztmp_h, vtmp_h = self.h_l.activity.get_activity()
        # 'imagine' what the activity will look like
        ztmp_h += date - self.h_l.activity.date
        vtmp_h *= np.exp(-np.divide(date - self.h_l.activity.date,
                                    self.h_l.activity.tau_mem_decay))
        cond_tmp = vtmp_h < self.h_l.activity.extinction_threshold
        itmp = cond_tmp.nonzero()
        vtmp_h = np.delete(vtmp_h,itmp)
        ztmp_h = np.delete(ztmp_h,itmp)

        if self.verbose_mode:
            print 'selfsize ', vtmp_self.size, 'melsize ', vtmp_mel.size,  'hsize ', vtmp_h.size

        vtmp_self *= self.s_w
        vtmp_mel *= self.m_w
        vtmp_h *= self.h_w
        ztmp, vtmp = merge(list(ztmp_self), list(vtmp_self),
                           list(ztmp_mel), list(vtmp_mel))
        ztmp, vtmp = merge(list(ztmp), list(vtmp), list(ztmp_h), list(vtmp_h))

        ztmp = np.array(ztmp)
        vtmp = np.array(vtmp)

        self.new_event_histo.append([(list(ztmp_self), list(vtmp_self)), (list(ztmp_mel), list(vtmp_mel)), (list(ztmp_h), list(vtmp_h))])


        # interaction w/ pulsative time
        if self.phase_influence:
            vtmp *= np.exp(self.gamma*(np.cos(
                        2*np.pi*(ztmp-date+self.phase_ref))-1))


        # modulate -- repellor at the end
        modulate_activity(ztmp, vtmp, self.s_l.event_list[-1], 0.001, 4.0)


        # experimental taboo based on timed values
        # 'classic' taboo based on number of states is straightforward
        ind_end = len(self.s_l.event_history)
        ind_tmp = ind_end-1
        while (ind_tmp > 0 and
            (date - self.s_l.event_history[ind_tmp][0]) < self.taboo_length+0.5*self.b_step):
            # find taboo mod factor
            ind_taboo_tmp = int(np.round((date - self.s_l.event_history[ind_tmp][0])/self.b_step))
            if ind_taboo_tmp > 0:
                modulate_activity(ztmp, vtmp,
                                self.s_l.event_list[self.s_l.event_history[ind_tmp][1]],
                                self.taboo_params[-ind_taboo_tmp], 0.2*self.b_step)
            ind_tmp = ind_tmp-1



        if self.prepare_to_jump:
            self.prepare_to_jump = 0
        else:
            # modulate -- next state
            modulate_activity(ztmp, vtmp,
                self.s_l.event_list[self.s_l.event_history[-1][1]]+
                date-self.s_l.event_history[-1][0], self.next_state, 0.05)

#        # add noise
#        vtmp += np.random.normal(0, 0.4, vtmp.size)

        if vtmp.size == 0:
            result = self.s_l.event_history[-1][1] + 1
        else:
            t_width = 0.1

            maxtmp = 0.0
            efinal = -1

            # todo: keep all the maxs and rand pick one
            for i in range(len(ztmp)):
                if vtmp[i] >= maxtmp:
                    itmp, dtmp = find_closest_element(self.s_l.event_list, ztmp[i])
                    vfinaltmp = vtmp[i]*np.exp(-dtmp*dtmp/(2*t_width*t_width))
                    if vfinaltmp > maxtmp:
                        maxtmp = vfinaltmp
                        efinal = itmp


            if efinal == -1:
                result = self.s_l.event_history[-1][1] + 1
                if self.verbose_mode:
                    print '----------------- no event found -----------------'
            else:
                result = efinal

            if result >= len(self.s_l.event_list):
                result = 1


        if self.adjust_phase:
            diff_phase_target = (np.mod(self.s_l.event_list[result], 1.0) -
                                np.mod(date-self.phase_ref, 1.0))
            if diff_phase_target > 0.:
                diff_phase_target = diff_phase_target - 1.0

            new_date = date + diff_phase_target

            if new_date < date - self.phase_adjustment_w[0]:
                new_date = new_date + 1.0
            if new_date > date + self.phase_adjustment_w[1]:
                new_date = date # outside window; do not make any adjustment
        else:
            new_date = date

        self.s_l.event_history.append([new_date, result])
        return result, new_date

    def jump(self):
        self.prepare_to_jump = 1
        self.s_l.activity.insert(
            [self.s_l.event_list[self.s_l.event_history[-1][1]]
            -(self.s_l.event_history[-1][0]-self.s_l.activity.date)], [-10.0])
        self.m_l.activity.insert(
            [self.s_l.event_list[self.s_l.event_history[-1][1]]
            -(self.s_l.event_history[-1][0]-self.m_l.activity.date)], [-10.0])
        self.h_l.activity.insert(
            [self.s_l.event_list[self.s_l.event_history[-1][1]]
            -(self.s_l.event_history[-1][0]-self.h_l.activity.date)], [-10.0])

    def adjust_bpm(self, current_bpm, min_bpm, max_bpm, date):
        ext_ev_tmp = np.array(get_elements_within_win(self.s_l.external_events,
                             self.s_l.external_events.size-1,
                             self.w_length*60000./current_bpm))
        if ext_ev_tmp.size <= 2:
            best_bpm = current_bpm
        else:
            if len(self.s_l.event_history) > 1:
                zeta_tmp = self.s_l.event_list[self.s_l.event_history[-1][1]]+date-self.s_l.event_history[-1][0]
                ev2tmp, dtmp = find_closest_element(self.m_l.event_list, zeta_tmp)
                psi_ref_tmp = np.array(
                    get_elements_within_win(self.m_l.event_list, ev2tmp, self.w_length+1.0))
                if psi_ref_tmp.size <= 2:
                    psi_ref_tmp = round(self.w_length) - np.linspace(0,
                                            round(self.w_length),round(self.w_length)+1)
                else:
                    psi_ref_tmp = psi_ref_tmp[-1] - psi_ref_tmp
            else:
                psi_ref_tmp = 5. - np.linspace(0,5.,6)

            best_bpm = compute_best_bpm(current_bpm,
                                             [max(min_bpm / current_bpm, 0.9),
                                              min(max_bpm / current_bpm, 1.1)],
                                            ext_ev_tmp, psi_ref_tmp, 0.01)
        return best_bpm




# very primitive idea...
def compute_best_bpm(current_bpm, alpha_range, event_history, psi_ref, w_step):
    psi_alpha = current_bpm/60000. * event_history
    psinow = psi_alpha[-1]
    psialpha = psinow - psi_alpha[::-1]
    t_width = 0.02
    alpha_rg = np.arange(alpha_range[0],alpha_range[1], w_step)
    olp = np.zeros(alpha_rg.size)
    for k in range(0,alpha_rg.size):
        olptmp = 0 # some sort of OverLaP
        jold = 1
        psialpha_tmp = list(alpha_rg[k]*psialpha)
        for i in range(1,psi_ref.size):
            # use the fact that both lists are sorted
            j_tmp, d_tmp = find_closest_element(psialpha_tmp[jold:], psi_ref[i])
            eij = np.exp(-0.25*np.power(d_tmp/t_width,2))
            olptmp = olptmp + eij
            jold = j_tmp+1
        olp[k] = olptmp
    ind_tmp = find_max_peak(olp)
    if ind_tmp == -1: # no peak
        best_bpm = current_bpm
    else:
        best_bpm = current_bpm * alpha_rg[ind_tmp]
    return best_bpm





def get_elements_within_win(list_arg, ind_end, w_length):
    ind_tmp = ind_end
    while (ind_tmp > 0 and (list_arg[ind_end] - list_arg[ind_tmp]) < w_length):
        ind_tmp = ind_tmp - 1
    return list_arg[ind_tmp:ind_end+1]


def find_max_peak(values):
    max_tmp = -1 #means no value found yet; assume positive values for now
    ind_tmp = -1 #means no value; not the last element, as in python
    for i in range(1, values.size-1):
        # it's a peak, and it's higher than the previous ones
        if (values[i] > values[i-1] and values[i] >= values[i+1]
        and values[i] > max_tmp):
            max_tmp = values[i]
            ind_tmp = i
    return ind_tmp#, max_tmp



 # put that and more in a seq_utilities package
def argmax_list(seq):
    if seq.size == 0:
        result = np.array([])
    else:
        result =  np.argwhere(seq == np.amax(seq))
    return result.flatten()

def argmax_rand(seq):
    if seq.size > 0:
        tmp = argmax_list(seq)
        result = np.random.choice(tmp)
    else:
        result = 0
        # should raise an exception instead'
    return result



def modulate_activity(zeta_list, value_list, zeta_pos, mod_value, mod_width=0.5):
    #mod_width = 0.5
    itmp0 = zeta_list.searchsorted(zeta_pos)
    itmp = itmp0
    # inhibit to the right
    while  (itmp < zeta_list.size
            and np.abs(zeta_pos-zeta_list[itmp]) < mod_width):
        value_list[itmp] = scale_activity(value_list[itmp]*mod_value)
        itmp += 1
    itmp = itmp0 - 1
    # inhibit to the left
    while  itmp >= 0 and np.abs(zeta_pos-zeta_list[itmp]) < mod_width:
        value_list[itmp] = scale_activity(value_list[itmp]*mod_value)
        itmp -= 1



def merge(list1, value1,  list2, value2):
    t_width = 0.1 #should be a, outside parameter...
    if len(list1) == 0:
        return list2, value2
    elif len(list2) == 0:
        return list1, value1
    else:
        result = list()
        value = list()
        itmp_old = 0
        list1_len = len(list1)
        for i in range(0,len(list2)):
            new_elt = list2[i]
            new_value = value2[i]
            itmp = bisect.bisect_left(list1[itmp_old:], new_elt)
            itmp += itmp_old
            result.extend(list1[itmp_old:itmp])
            value.extend(value1[itmp_old:itmp])
            if len(result) and np.abs(new_elt-result[-1]) < 0.9*t_width: # remove len
                # modify it
                result[-1] = ((value[-1]*result[-1]+new_value*new_elt)
                                /(value[-1]+new_value))
                value[-1] = value[-1]+new_value
                itmp_old = itmp
            elif itmp < list1_len and np.abs(new_elt-list1[itmp]) < 0.9*t_width:
                # modify and add it
                new_elt = ((value1[itmp]*list1[itmp]+new_value*new_elt)
                                /(value1[itmp]+new_value))
                new_value = value1[itmp]+new_value
                result.append(new_elt)
                value.append(new_value)
                itmp_old = itmp + 1
            else:
                # simply add it
                result.append(new_elt)
                value.append(new_value)
                itmp_old = itmp
        # add the last elements
        result.extend(list1[itmp_old:])
        value.extend(value1[itmp_old:])
        return result, value


# returns index of closest elemnt in a sorted list of x to x_target
# as well as the corresponding distance
def find_closest_element(list_of_x, x_target):
    ind_tmp = bisect.bisect_left(list_of_x, x_target)
    if (ind_tmp == len(list_of_x)):
        dist_tmp = np.abs(list_of_x[ind_tmp-1] - x_target)
        ind_tmp = ind_tmp-1
    else:
        dist_tmp_r = np.abs(list_of_x[ind_tmp] - x_target)
        dist_tmp = dist_tmp_r
        if (ind_tmp > 0):
            dist_tmp_l = np.abs(list_of_x[ind_tmp-1] - x_target)
            if dist_tmp_l < dist_tmp_r:
                ind_tmp = ind_tmp - 1
                dist_tmp = dist_tmp_l
    return ind_tmp, dist_tmp




# max activity need to be some param
def scale_activity(activity):
    if activity.size == 1:
        if (activity > 5.0):
            new_activity = np.array(5.0)
        else:
            new_activity = activity
    else:
         new_activity = scale_activity_array(activity)
    return new_activity

def scale_activity_array(activity):
    cond_tmp = activity > 5.0
    itmp = cond_tmp.nonzero()
    new_activity = np.copy(activity)
    new_activity[itmp] = 5.0
    return new_activity
