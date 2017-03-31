import pandas as pd
s0 = ['A', 'B', 3]
s1 = ['Aa', 'BB', 7]


df = pd.DataFrame(columns =  ["A", "B", "C"])
df.loc[len(df)] = s0  # adding a row
df.loc[len(df)] = s1  # adding a row

#df = df.sort() 
print df
