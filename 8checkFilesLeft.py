import pandas as pd
import os.path

#==============================================================================
# dfs = pd.read_csv('all_files.csv')
# dfs.index = dfs['Unnamed: 0']
# dfs = dfs.drop(['Unnamed: 0'], axis = 1)
# removed = pd.read_csv('URLsToRemove.csv')
# removed.index = removed['Unnamed: 0']
# removed = removed.drop(['Unnamed: 0'], axis = 1)
# left = dfs[~dfs.isin(removed)].dropna()
# print len(left) + len(removed) == len(dfs)
# print left
#==============================================================================
ll = pd.read_csv('csv/filesLeft.csv')
ll = ll.drop(['Unnamed: 0'], axis = 1)
new = list(ll.new) 
idx = list(ll.idx)
pathfiles = []
indices = []

prefix = '../'
for i in range(len(ll)):
    if i % 10000 == 0:
        print i
    folder = 'new_' + str(int(new[i]))
    filename = str(int(idx[i])) + '.html'
    pathfile = folder + '/' + filename
    #print pathfile
    if os.path.isfile(prefix+pathfile):
        pathfiles.append(pathfile)
    else:
        print pathfile + ' removed!'
        indices.append(i)
ll = ll.drop(ll.index[indices])
ll['pathfile'] = pathfiles
ll = ll.drop(['new', 'idx'], axis = 1)
ll.to_csv('index.csv', index = False)
#ll = pd.read_csv('index.csv')
n = len(ll)
c = 0
for i in range(8):
    folder = prefix +'new_' + str(i) + '/'
    fnames = os.listdir(folder)
    c += len(fnames)
print c == n
