from adblockparser import AdblockRules
import pandas as pd
from multiprocessing import Pool


f = open('easylist.txt','r')
raw_rules = []
line = f.readline()
line = f.readline()
while line:
    line = line.strip()
    if line[0] != '!':
        raw_rules.append(line)
    line = f.readline()
f.close()

rules = AdblockRules(raw_rules)

df = pd.read_csv('csv/indexFirstRound.csv')
urls = list(df['url'])



def f(url):
    return rules.should_block(url)

            

if __name__ == '__main__':
    p = Pool(processes=12) 
    #urls = ['http://www.huffingtonpost.com/news/bridgegate/7/ads/zone/']
    records = p.map(f, urls)   
    data = df[records]
    data.to_csv('should_block.csv', index = False)
