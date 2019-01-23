import matplotlib.pyplot as plt
import numpy as np
import sys
import time

filename=sys.argv[1]
print('plot', filename)
#plt.ion()
while(True):
    ifile=open(filename)
    #for i,l in enumerate(ifile):
    l=ifile.readline()
    ifile.close()
    #title=l.split(',')[0]+' '+l.split(',')[1]
    data=l.split(',')
    data=np.array(data,dtype=np.float)
    print(data[:10])
    plt.plot(data,'-')
    #plt.draw()
    plt.show()
    #time.sleep(3)
    plt.close()
