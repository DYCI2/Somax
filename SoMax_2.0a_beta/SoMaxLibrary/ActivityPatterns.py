
import numpy as np
from bisect import bisect_left
from copy import deepcopy
from Tools import SequencedList

class AbstractActivityPattern(object):

    def __init__(self, date=0.0):
        self.zeta = np.array([], dtype=np.dtype(float)) # list of activity peaks dates
        self.value = np.array([], dtype=np.dtype(float)) # list of activity peaks heights
        self.transform = []
        self.date = date # current time of the activity state
        self.available = True

    def __repr__(self):
        return reduce(lambda x, y: x+"{0} at {1}".format(str(y[0]), str(y[1])), zip(self.zeta, self.value), "")

    def __desc__(self):
        return "Abstract Activity Pattern"

    def insert(self,z,a,t):
        print "Inserts activity peaks as sets (location, value, transform)"

    def get_activity(self, time=None):
        if time==None:
            time = int(self.date)
        return self.zeta, self.value, self.transform
        #print "returns activity"

    def update_activity(self, new_date):
        print "Forcasts activity profile at the wanted date."

    def clean_up(self):
        print "Cleans activities profile below extinction thresold"

    def reset(self, time):
        self.zeta = np.array([], dtype=np.dtype(float)) # list of activity peaks dates
        self.value = np.array([], dtype=np.dtype(float)) # list of activity peaks heights
        self.transform = []
        self.time = time


class ClassicActivityPattern(AbstractActivityPattern):
    tau_mem_decay = 2.0
    t_width = 0.1
    extinction_threshold = 0.1
    available = 1

    def __init__(self, date=0.0):
        super(ClassicActivityPattern, self).__init__(date)
    def __desc__(self):
        return "Classic Activity Pattern"

    def insert(self, *args):
        for peak in args:
            assert type(peak) is tuple and len(peak)==3, "peak insertion failed!"
            zeta, value, transform = peak
            i = bisect_left(self.zeta, zeta)
            self.zeta = np.insert(self.zeta, i, zeta)
            self.value = np.insert(self.value, i, value)
            self.transform.insert(i,transform)

    def update_activity(self, new_date):
        if self.available:
            self.available = 0
            self.zeta += new_date - self.date
            self.value *= np.exp(-np.divide(new_date - self.date, self.tau_mem_decay))
            self.date = new_date
            self.zeta, self.value, self.transform=self.clean_up(self.zeta, self.value, self.transform)
            self.available = 1

    def clean_up(self, zeta, value, transform):
        cond_tmp = value < self.extinction_threshold
        itmp = cond_tmp.nonzero()
        zeta = np.delete(zeta,itmp)
        value = np.delete(value,itmp)
        transform_tmp = deepcopy(transform)
        for i in reversed(sorted(itmp[0].tolist())):
            del transform_tmp[i]
        return zeta, value, transform_tmp

    def get_activity(self, date=None):
        if date==None:
            date = int(self.date)
        if self.available:
            self.available = 0
            ztmp = np.array(self.zeta)
            vtmp = np.array(self.value)
            ttmp = deepcopy(self.transform)
            self.available = 1
            ztmp+=date - self.date
            vtmp *= np.exp(-np.divide(date - self.date, self.tau_mem_decay))
            ztmp, vtmp, ttmp =  self.clean_up(ztmp, vtmp, ttmp)
            return SequencedList(list(ztmp), list(zip(vtmp, ttmp)))

        else:
            return np.array([]), np.array([]), np.arra
