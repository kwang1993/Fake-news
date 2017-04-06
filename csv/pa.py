import pandas as pd
df = pd.read_csv('all_files.csv')

print df['new' == 6 and 'idx' == 1000]
