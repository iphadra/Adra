#!/usr/bin/env python3

import os
import subprocess
import time
import os.path
import numpy as np
from CCD_lib import *

"""
Make script executable with:

$ chmod +x run_CCD.py

and run with

$ ./run_CCD.py
"""

i_time = 2200
scans = 30
mode = 0
trigout = 0
d_corr = 0

print("Iniciando...")
while True:
    """
    Never-ending loop.
    """

    # Wait this number of seconds before calling the code again.
    n_sec = 2
    #header file
    header = "dataraw/header.txt"
    #get time
    t1 = time.strftime("%Y-%m-%d_%H%M")
    t2 = time.strftime("%Y-%m-%d_%H%M")
    
    print(t1,t2)
    while(True):
        data = [np.zeros(3648)]
        while t1==t2:
            print('*', end='')
            # Call CCD executable.
            datafile = executeCCD(i_time,scans,mode,trigout,d_corr)
            print(data)
            with open(datafile,'r') as ipfile:
              for line in ipfile:
                datan = line[:-1].split(',')
                data = np.append(data,[datan],axis=0)
            data = data[1:].astype(np.int)
            print('data', data, np.size(data))
            print('prom',np.mean(data,axis=0))
            time.sleep(n_sec)
            t2 = time.strftime("%Y-%m-%d_%H%M")
        print(t2)
        t1 = t2
        t = time.strftime("%Y-%m-%d")
        h = time.strftime("%H:%M:00")
        ofilename = "data/CCD-prom-"+t+".csv"
        gfile="data/gfile.csv"
        if os.path.isfile(ofilename):
           newfile = False
        else:
           newfile = True
        #header
        opfile = open(ofilename, 'a')
        if newfile == True:
            with open(header,'r') as ipfile:
                for line in ipfile:
                    print(line, end='', file=opfile)
        prom=np.mean(data,axis=0)
        str_prom = ''
        for d in prom:
           str_prom += str(d)+','
        str_prom=str_prom[:-1]
        print(t,h,i_time, str_prom, sep=',',file=opfile)
        with open(gfile,'w') as tmpfile:
            print(t,h,i_time, str_prom, sep=',',file=tmpfile)
         
#*************************************************************
    # Wait this number of seconds before calling the code again.
    n_sec = 2
    #create_header('dataraw/header.txt','data/out.csv')
    #os.('dataraw/')
    time.sleep(n_sec)
    # Call CCD executable.
    datafile = executeCCD(i_time,scans,mode,trigout,d_corr)
    if not os.path.isfile(datafile):
        continue
    print('test=',datafile)
    create_ofile(datafile,header)
