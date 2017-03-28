import pandas as pd
import ast
import json
import os
#filename = 'filesLeftWithoutEmptyFiles.csv'
filename = 'indexFirstRound.csv'
print filename
df = pd.read_csv(filename)
urls = list(df.url)
#print urls
print len(urls)
print '\n'

dataframe = pd.DataFrame(columns =  ["wanefile", 'url', 'timestamp', 'named_entities', 'digest'])
url = []
folder = 'wane/'
fnames = os.listdir(folder)
for fname in fnames:
    print fname
    pathfile = folder + fname
    f = open(pathfile, 'r')
    data = f.readlines()
   
    n_records = 0
    c = 0
    for line in data:
        line = line.strip()
        dic = ast.literal_eval(line)
        #print dic['url']
        n_records += 1
        if dic['url'] not in urls:
            c += 1
            dataframe.loc[len(dataframe)] = [fname, dic['url'], dic['timestamp'], dic['named_entities'], dic['digest']]


    f.close()
    print n_records
    print c

    
dataframe.to_csv('waneCompare.csv', index = False)
