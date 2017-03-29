import pandas as pd
from boilerpipe.extract import Extractor
import os
from multiprocessing import Pool

def f(i):
    df = pd.DataFrame(columns = ['pathfile', 'content'])
    path = 'new_'+str(i) + '/'
    print path
    fnames = os.listdir(path)
    c = 0 
    for fname in fnames:
        c += 1
        if c % 100 == 0:
            print c
        pathfile= path + fname
        f = open(pathfile, 'r')
        data = ''
        line = f.readline()
        while line:
            data += line
            line = f.readline()
        f.close()
        extractor = Extractor(extractor='ArticleExtractor', html=data)
        content = extractor.getText()
        # print content
        df.loc[len(df)] = [pathfile, content]
    df.to_csv('contents'+str(i)+'.csv', index = False)

if __name__ == '__main__':
    p = Pool(processes=4) 
    p.map(f, [0,1,2,7]) 







        
