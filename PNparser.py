#!/usr/bin/python 

# PhysioNoise files parser.
# vittorio.iacovella@gmail.com
# 2013.05.03
# ---
# Usage:
# $./PNparser.py fileName sampFreq TR totScans dummyScans outFileName
# where:
# sampFreq is the sampling frequency of the physioNoise data;
# TR is the repetition time of the scans;
# totScans is the number of the scans you have in the session;
# dummyScans is the initial number of scans you have to avoid.
# ---
# CODE:

# Dictionaries:

import sys

# ArgIn 

sampFreq=int(sys.argv[2])
TR=float(sys.argv[3])
totScans=int(sys.argv[4])
dummyScans=int(sys.argv[5])
theOutFilename=sys.argv[6]

# Some computations

totSamples=int(sampFreq*TR*totScans)
dummySamples=int(dummyScans*TR*sampFreq)

# File Operations:

inFile = open(sys.argv[1])
print inFile.name
outFile=open(theOutFilename,"w")
myVec = file.readlines(inFile)
inFile.close

# Parsing.1: Split file into rows, seek the 'SecToStart' flag, neglect the footer, clean the residual flags

secPos = myVec[0].find('Sec') - 1
secToSkip=int(myVec[0][secPos]) 
print "Seconds To Skip:",secToSkip 
myVeClean=myVec[0].replace('\r\n',' ')

# Parsing.2: delete the non-interesting samples: the header; samples before the acquisition; samples after the acquisition; dummy scans.

myVeClean=myVeClean[secPos+12:]
myVeClean=myVeClean[1:-1].split(' ')

myVeClean=myVeClean[secToSkip*sampFreq:]

myVeClean=myVeClean[0:totSamples]

myVeClean=myVeClean[dummySamples:]

# Save the work
#myStrClean=str(myVeClean)
#myStrClean=myStrClean.replace(' ','\n')
#myStrClean.append('\n')

for i in myVeClean:
  print >> outFile, i

#toutFile.writelines(myVeClean) # Writes the file
print outFile.name
outFile.close
