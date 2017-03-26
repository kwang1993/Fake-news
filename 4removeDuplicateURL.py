import pandas as pd
import os.path


removed = pd.read_csv('URLsToRemove.csv')

new = list(removed.new) 
idx = list(removed.idx)
for i in range(len(new)):
    folder = 'new_' + str(int(new[i]))
    filename = str(int(idx[i])) + '.html'
    pathfile = folder + '/' + filename
    #print pathfile
    if os.path.isfile(pathfile):
        os.system('rm '+ pathfile)

