#This program identifies the top 10 files which have the largest size on the system in the given directory

import os
import operator
import heapq

directory = '/home' #LINUX
#directory = 'C:/Users/VINEETH'
n = 10 #Number of files

def allfiles(directory):
    for dirpath, _, filenames in os.walk(directory): #Loop through each file and return their sizes
        for eachfile in filenames:
            fullname = os.path.join(dirpath, eachfile)
            if(os.path.exists(fullname)):
                yield fullname, os.path.getsize(fullname)

topfiles = heapq.nlargest(n, allfiles(directory), key=operator.itemgetter(1)) #Sort the files based on their sizes
for f in topfiles: #Print the top 10 files
    b=float(f[1])
    b=b/(1024**2)
    print("{0}\t{1:.2f}MB".format(f[0],b))
