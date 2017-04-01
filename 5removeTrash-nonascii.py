# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 13:33:42 2017

@author: wangkaicheng
"""
import shutil
import os.path
from guess_language import guessLanguage

prefix = '../'
def checkfile(fname):
    f = open(prefix + fname + '.txt', 'r')
    data = ''
    line = f.readline()
    while line:
        data += line
        line = f.readline()
    f.close()
    if guessLanguage(data) != 'en':
        print fname
        shutil.move(prefix + fname, '../nonascii/' + fname)
        shutil.move(prefix + fname + '.txt', '../nonascii/' + fname + '.txt')

for i in range(4,8):

    path = "new_"+ str(i)+'/'
    print path
    if os.path.isdir(prefix + path):
        ls = os.listdir(prefix + path)
        ls = [l for l in ls if l[-5:] == '.html']
        for fname in ls:
            checkfile(path+fname) 
