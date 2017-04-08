import pandas as pd
import os

ll = pd.read_csv('index.csv')
n = len(ll)

c = 0
for i in range(8):
    folder = 'new_' + str(i) + '/'
    names = os.listdir(folder)
    fnames = [fname for fname in names if fname[-5:] =='.html']
    c += len(fnames)
    print '{0}: {1}'.format(folder, len(fnames))
print 'payload number = %d' % c
print 'len(index) = %d' % n
print 'len(index) == payload number: {0}'.format(c == n)
print 'payload number == contents extracted: {0}'.format(len(fnames) == len(names) - len(fnames))
