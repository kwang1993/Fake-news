# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 13:33:42 2017

@author: wangkaicheng
"""
import shutil
import os.path
 
prefix = '../'
def checkfile(fname):
    f = open(prefix + fname + '.txt', 'r')
    data = f.readlines()
    f.close()
    eflag = 0
    #ls = ['page', 'unavailable']
    ls = [ 'function', 'return', 'var' ]
    for line in data:
        c = 0
        line = line.lower()
        for l in ls:
            if l in line:
                c+=1
                if c >= 3:
                    print line
                    eflag = 1
                    break
        if eflag:
            break

    if eflag:
        print fname
        shutil.move(prefix + fname, '../trash/' + fname)
        shutil.move(prefix + fname + '.txt', '../trash/' + fname + '.txt')

for i in range(8):

    path = "new_"+ str(i)+'/'
    print path
    if os.path.isdir(prefix + path):
        ls = os.listdir(prefix + path)
        ls = [l for l in ls if l[-5:] == '.html']
        for fname in ls:
            checkfile(path+fname) 
