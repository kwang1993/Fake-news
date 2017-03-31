import pandas as pd
from boilerpipe.extract import Extractor
import os
from guess_language import guessLanguage
from multiprocessing import Pool


    
def isEnglish(text):
    return guessLanguage(text) == 'en'
               
def isCode(text):
    code = ['function', 'return', 'var', 'prototype','instanceof','typeof', 'void',
            'src', 'iframe']
    for token in code:
        if token in text.lower():
            return 1
    return 0

def isAd(text):
    keywords = ['ticket', 'discount', 'free', 'sign in', 'facebook', 'swim',
                'game', 'available', 'movie', 'snack', 'restaurant' ]
    for w in keywords:
        if w in text.lower():
            return 1
    return 0   

def isNews(text):
    keywords = ['christie', 'columnist', 'governor', 'investigate', 'testimony',
                'media group' ]
    for w in keywords:
        if w in text.lower():
            return 1
    return 0

def f(i):
    pathfiles = []
    contents = []
    path = 'new_'+str(i) + '/'
    print path
    fnames = os.listdir(path)
    htmls = [fname for fname in fnames if fname[-5:] == '.html']
    for html in htmls:        
        pathfile= path + html
        txt = pathfile + '.txt'
        print pathfile
        print '---------------'
        if txt in fnames:
            pass
##            f = open(txt, 'r')
##            content = f.readlines()
##            f.close()
        else:
            f = open(pathfile, 'r')
            data = ''
            line = f.readline()
            while line:
                data += line
                line = f.readline()
            f.close()
            extractor = Extractor(extractor='ArticleExtractor', html=data)
            content = extractor.getText()
            fout = open(txt, 'w')
            fout.writelines(content.encode('utf-8'))
 
##        if isEnglish(content) and (not isCode(content)) and isNews(content):
##            pathfiles.append(pathfile)
##            contents.append( content )
##            if len(content) > 1000:
##                print content[:1000]
##            else:
##                print content
##            print '---------------'
##            print 'Yes'
##        else:
##            if len(content) > 100:
##                print content[:100]
##            else:
##                print content
##            print '---------------'
##            print 'No'
##        print '=================\n'
##            
##    df = pd.DataFrame({'pathfile': pathfiles,
##                       'content': contents})    
##    df.to_csv('contents'+str(i)+'.csv', index = False, encoding='utf-8')




if __name__ == '__main__':
    p = Pool(processes=8) 
    p.map(f, [0,1,2,3,4,5,6,7])



        
