# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 13:33:42 2017

@author: wangkaicheng
"""
import os
import os.path
 
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
    filename = filenames[i]
    if os.path.isfile(filename):
        if not os.path.isfile(path) :
            print "warcindex... "+path
            os.system("warcindex "+ filename +" | grep response | more > "+path)
   

    
    
