import matplotlib.pyplot as plt
import numpy as np
import sys
import time

filename=sys.argv[1]
print('plot', filename)
plt.ion()
fig=plt.figure()

while(True):
    ifile=open(filename)
    #for i,l in enumerate(ifile):
    l=ifile.readline()
    ifile.close()
    #title=l.split(',')[0]+' '+l.split(',')[1]
    data=l.split(',')
    try:
        data=np.array(data,dtype=np.float)
    except:
        pass
    print(data[:10])
    fig.clf()
    plt.axis((0,4000,0,66000))
    plt.title(time.strftime("%d %b  %Y %H:%M:%S -0600",time.localtime()))
    plt.plot(data,'-')
    fig.canvas.draw()
    fig.canvas.flush_events()
    #plt.draw()
    #plt.show()
    time.sleep(3)
    #plt.close()
