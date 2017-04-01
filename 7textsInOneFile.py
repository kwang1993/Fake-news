import json
import pandas as pd
from pprint import pprint
import os, os.path
from multiprocessing import Pool
from collections import OrderedDict

prefix = '../'
index = pd.read_csv('index.csv')

def f(i):
    path = 'new_'+str(i)+'/'
    print path
    files = os.listdir(prefix + path)
    files = [f for f in files if f[-5:] == '.html']
    result = 'result_'+str(i)+'.txt'
    if os.path.isfile(result):
        os.remove(result)
    fout = open(result, 'a')
    for fname in files:
            html = path + fname
            txt = html + '.txt'
            try:
                url = list(index['url'][index['pathfile'] == html])[0]
            except:
                print html
                url = ''
            f = open(prefix + txt, 'r')
            text = ''.join(f.readlines())
            f.close()

            dic = OrderedDict([('name',html), ('url',url), ('text',text)])
            fout.write(json.dumps(dic.items()).encode('utf-8') + '\n')
    fout.close()



if __name__ == '__main__':
    p = Pool(processes=2) 
    p.map(f, range(5,8)) 
