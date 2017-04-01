# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 13:33:42 2017

@author: wangkaicheng
"""
import os
import os.path
 
    
def checkfile(fname):
    print "checkfile " + fname
    f = open(fname, 'r')
    data = f.readlines()
    f.close()
    eflag = 0
    tflag = 1
    ls = ['not found', '404 error', 'cannot be found', 'server error', 'http status 404']
    for line in data:
        line = line.lower()
        for l in ls:
            if l in line:
                eflag = 1
                break
        if eflag:
            break
        if '</html>' in line:
            tflag = 0
            break
    if eflag or tflag:
        os.system("rm "+fname)


for i in range(8):

    path = "../new_"+ str(i)+'/'
    if os.path.isdir(path):
        ls = os.listdir(path)
        for fname in ls:
            checkfile(path+fname) 
