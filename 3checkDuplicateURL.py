import pandas as pd

dfs = pd.DataFrame()
for i in range(8):
    df = pd.read_csv('list_'+str(i)+'.csv')
    dfs = pd.concat([dfs, df], ignore_index = True)

print len(dfs)
dfs.columns
dfs = dfs.drop(['Unnamed: 0'], axis = 1)
dfs.to_csv('all_files.csv')
duplicates = dfs[dfs.duplicated(subset = 'url', keep=False)].sort_values(by = ['url','size'])
duplicates.to_csv('duplicateURL.csv', columns = dfs.columns)
removed = duplicates[duplicates.duplicated(subset = 'url', keep = 'last')].sort_values(by = ['url','size'])
removed.to_csv('URLsToRemove.csv', columns = dfs.columns)
duplicates.isin(dfs)
left = dfs[~dfs.isin(removed)].dropna() # drop rows with FALSE
left.to_csv('filesLeft.csv', columns = dfs.columns)
print len(left) + len(removed) == len(dfs)
#==============================================================================
# ll = pd.read_csv('filesLeft.csv')
# ll.index = ll['Unnamed: 0']
# ll = ll.drop(['Unnamed: 0'], axis = 1)
# ll.equals(left)
#==============================================================================
