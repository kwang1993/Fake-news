from adblockparser import AdblockRules
import pandas as pd

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
boolean = [rules.should_block(url) for url in list(df['url'])]
data = df[boolean]
data.to_csv('should_block.csv', index = False)
