from numpy import array, exp, where, log2, floor, ceil, zeros, log, arange, round, maximum, ones_like, power, dot, transpose
from scipy import io
import bisect, itertools, operator

def computePitchClassVector(noteMatrix, tStep = 20.0, thresh=0.05, m_onset=0.5, p_max=1.0, tau_up=400, tau_down=1000, decayParam=0.5):
	nbNotes = len(noteMatrix)
	matrix = array(noteMatrix)
	tRef = min(matrix[:, 5])
	matrix[:,5] -= tRef
	tEndOfNM = max(matrix[:, 5] + matrix[:, 6]) + 1000
	nbSteps = ceil(tEndOfNM/tStep)
	pVector = zeros((128, int(nbSteps)))
	mVector = zeros((12, int(nbSteps)))
	nbMaxHarmonics = 10;

	for i in range(0, nbNotes):
		if (matrix[i,5]==0):
			t_on = 0.0
		else:
			t_on = matrix[i, 5]

		t_off = t_on+matrix[i, 6]

		ind_t_on = floor(t_on/tStep)
		ind_t_off = floor(t_off/tStep)

		p_t_off = (m_onset - p_max)*exp(-(t_off-t_on)/tau_up) + p_max
		t_end = min(tEndOfNM, t_off - tau_down*log(thresh/p_t_off))
		ind_t_end = floor(t_end/tStep)

		p_up = (m_onset - p_max)*exp(-(arange(ind_t_on,ind_t_off)*tStep-t_on)/tau_up) + p_max
		p_down = p_t_off*exp(-(arange(ind_t_off,ind_t_end)*tStep-t_off)/tau_down)

		ind_p = matrix[i, 3] # + 1?
		ind_p, ind_t_on, ind_t_off, ind_t_end =  int(ind_p), int(ind_t_on),int(ind_t_off), int(ind_t_end)
		pVector[ind_p,ind_t_on:ind_t_off] = maximum(pVector[ind_p, ind_t_on:ind_t_off], p_up)
		pVector[ind_p,ind_t_off:ind_t_end] = maximum(pVector[ind_p,ind_t_off:ind_t_end], p_down)


		listOfMidiHarmonics = matrix[i,3] + round(12*log2(1 + arange(1,nbMaxHarmonics)))
		listOfMidiHarmonics = listOfMidiHarmonics[where(listOfMidiHarmonics<128)].astype(int)

		if listOfMidiHarmonics.size!=0:
			pVector[listOfMidiHarmonics, ind_t_on:ind_t_off] = maximum(pVector[listOfMidiHarmonics, ind_t_on:ind_t_off], \
				dot(power(ones_like(listOfMidiHarmonics)*decayParam, arange(1, listOfMidiHarmonics.size+1)).reshape(listOfMidiHarmonics.size, 1),p_up.reshape(1, p_up.size)))

			pVector[listOfMidiHarmonics, ind_t_off:ind_t_end] = maximum(pVector[listOfMidiHarmonics, ind_t_off:ind_t_end], \
				dot(power(ones_like(listOfMidiHarmonics)*decayParam, arange(1, listOfMidiHarmonics.size+1)).reshape(listOfMidiHarmonics.size, 1),p_down.reshape(1, p_down.size)))


	for k in range(0, 128):
		ind_pc = k % 12
		mVector[ind_pc, :] = mVector[ind_pc, :] + pVector[k,:]
	return mVector, tRef

def splitMatrixByChannel(matrix, fgChannels, bgChannels):
	fgMatrix = []
	bgMatrix = []
	for i in range(0, len(matrix)):
		if matrix[i][2] in fgChannels:
			fgMatrix.append(matrix[i])
		if matrix[i][2] in bgChannels:
			bgMatrix.append(matrix[i])
	return fgMatrix, bgMatrix

def getPitchContent(data, stateNb, legato):
	nbNotesInSlice = len(data[stateNb]["notes"])
	tmpListOfPitches = []
	for k in range(0, nbNotesInSlice):
		if (data[stateNb]["notes"][k]["note"][1]>0)\
			or (data[stateNb]["notes"][k]["time"][0] > legato):
			tmpListOfPitches.append(data[stateNb]["notes"][k]["note"][0])

	return list(set(tmpListOfPitches))

def most_common(L):
	# get an iterable of (item, iterable) pairs
	SL = sorted((x, i) for i, x in enumerate(L))
	# print 'SL:', SL
	groups = itertools.groupby(SL, key=operator.itemgetter(0))
	# auxiliary function to get "quality" for an item
	def _auxfun(g):
		item, iterable = g
		count = 0
		min_index = len(L)
		for _, where in iterable:
			count += 1
			min_index = min(min_index, where)
		# print 'item %r, count %r, minind %r' % (item, count, min_index)
		return count, -min_index
	# pick the highest-count/earliest item
	return max(groups, key=_auxfun)[0]

def get_beat(onset, beats):
	indice = bisect.bisect_left(beats, onset) # insertion index of the onset in the beats
	current_beat = indice # get the current beat
	try:
		current_beat += numpy.round((onset*1.0-beats[indice])/(beats[indice+1]-beats[indice]), 1)
	except:
		pass
	return current_beat
