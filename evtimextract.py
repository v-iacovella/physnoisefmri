import numpy as np
import matplotlib.pyplot as plt
import sys

# This python script should be ran from a terminal in this way:
# python evtimextract.py in_file.ext out_file.ext

# Command line arguments and I/O

in_file_name=sys.argv[1]
out_file_name=sys.argv[2]
raw_data=np.loadtxt(in_file_name)[:,1]

# Removing the mean: beats should now be positive

no_mean=raw_data - np.mean(raw_data)

# Isolating single beats periods by individuating starts and ends
# This is done by evaluating the sign function of the signal to obtain a sort of boxcar version of the cardiac trend. 
# Then the derivative values would tell whether the the switch is a "start" or an "end"

the_starts=np.argwhere(np.diff(np.sign(no_mean))==2)
the_ends=np.argwhere(np.diff(np.sign(no_mean))==-2)

# Getting rid of potential initial mismatching between starts and ends

if(np.min(the_starts)>np.min(the_ends)):
	the_ends=np.delete(the_ends,0)

# Reshaping to deal with handy objects

the_starts.reshape(the_starts.shape[0])
the_ends.reshape(the_ends.shape[0])

# Initializing a couple matrices to contain the results

periods_length=np.zeros(the_starts.shape[0])
ev_times = np.zeros(the_starts.shape[0])

# Evaluating the maximum value within a beat period. This should be by definition the beat

n=0
for p in np.arange(the_starts.shape[0] -1 ):
	curr_period=np.arange(the_starts[p],the_ends[p])
	periods_length[n]=curr_period.shape[0]
	ev_times[n] = the_starts[p] + np.argmax(raw_data[curr_period])
	n=n+1
ev_times=np.delete(ev_times,[the_starts.shape[0]-2,the_starts.shape[0]-1])

# Saving cardiac event times into a text files 

np.savetxt(out_file_name,ev_times,fmt='%d')

# Plot

#plt.plot(raw_data)
#plt.plot(ev_times,raw_data[ev_times.astype(int)],'r.')
