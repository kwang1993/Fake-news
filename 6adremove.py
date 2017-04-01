import pandas as pd
import shutil
df = pd.read_csv('csv/should_block.csv')
for pathfile in list(df['pathfile']):
    html = '../'+ pathfile
    txt = html + '.txt'
    shutil.move(html, '../ad/'+pathfile)
    shutil.move(txt, '../ad/'+pathfile+'.txt')

