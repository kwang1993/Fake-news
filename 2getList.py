# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 13:33:42 2017

@author: wangkaicheng
"""
import os
import os.path
import pandas as pd
 
filenames = ['ARCHIVEIT-8424-ONE_TIME-JOB260453-20170113223854038-00000.warc.gz',
'ARCHIVEIT-8424-ONE_TIME-JOB260736-20170116092423279-00001.warc.gz',
'ARCHIVEIT-8424-ONE_TIME-JOB260736-20170116093258354-00002.warc.gz',
'ARCHIVEIT-8424-ONE_TIME-JOB260736-20170116125225105-00003.warc.gz',
'ARCHIVEIT-8424-ONE_TIME-JOB260736-20170117090132777-00004.warc.gz',
'ARCHIVEIT-8424-ONE_TIME-JOB260736-20170118033455765-00005.warc.gz',
'ARCHIVEIT-8424-ONE_TIME-JOB260736-20170118204012997-00006.warc.gz',
'ARCHIVEIT-8424-ONE_TIME-JOB260736-20170116085642516-00000.warc.gz']



  
for i in range(len(filenames)):
    
    path = str(i)+'.txt'
    print "warcpayload..."+ path
    filename = filenames[i]
    df = pd.DataFrame(columns = ['url','size','new', 'idx'])
    if os.path.isfile(path) and os.path.isfile(filename):
        bufsize = 4096
        idx=0
        with open(path) as infile: 
            while True:
                lines = infile.readlines(bufsize)
                if not lines:
                    break
                for line in lines:
                    ls = line.strip().split()

                    if int(ls[-1]) > 1000:
                            offset = ls[1]
                            url = ls[3]
                            size = ls[-1]
                            directory = "./new_"+str(i)
                            if not os.path.exists(directory):
                                print "makedirs... "+directory
                                os.makedirs(directory)
                            f = directory + '/' + str(idx) + '.html'
                            
                            df.loc[len(df)] = [url, size, i, idx]
                            if idx % 1000 == 0:
                                print "warcpayload... "+ str(idx)
                            #os.system("warcpayload " + filename + ":"+ offset + " > "+ f)
                            idx += 1
 
        df.to_csv('list_'+str(i) +'.csv',encoding='utf-8')
   
