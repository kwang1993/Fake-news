import pandas as pd
from boilerpipe.extract import Extractor
import os
from guess_language import guessLanguage
from multiprocessing import Pool


##    
##def isEnglish(text):
##    return guessLanguage(text) == 'en'
##               
##def isCode(text):
##    code = ['function', 'return', 'var', 'prototype','instanceof','typeof', 'void',
##            'src', 'iframe']
##    for token in code:
##        if token in text.lower():
##            return 1
##    return 0
##
##def isAd(text):
##    keywords = ['ticket', 'discount', 'free', 'sign in', 'facebook', 'swim',
##                'game', 'available', 'movie', 'snack', 'restaurant' ]
##    for w in keywords:
##        if w in text.lower():
##            return 1
##    return 0   
##
##def isNews(text):
##    keywords = ['christie', 'columnist', 'governor', 'investigate', 'testimony',
##                'media group' ]
##    for w in keywords:
##        if w in text.lower():
##            return 1
##    return 0

def f(html):
    print html
    txt = html + '.txt'        
    f = open(html, 'r')
    data = ''
    line = f.readline()
    while line:
        data += line
        line = f.readline()
    f.close()
    extractor = Extractor(extractor='ArticleExtractor', html=data)
##    - DefaultExtractor
##    - ArticleExtractor
##    - ArticleSentencesExtractor
##    - KeepEverythingExtractor
##    - KeepEverythingWithMinKWordsExtractor
##    - LargestContentExtractor
##    - NumWordsRulesExtractor
##    - CanolaExtractor
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
    p = Pool(processes=10) 
    for i in range(8):
        path = 'new_'+str(i) + '/'
        print path
        names = os.listdir(path)
        fnames = []
        for fname in names:
           fnames.append(path + fname)

        htmls = [fname for fname in fnames if fname[-5:] == '.html' and fname + '.txt' not in fnames]
        
        p.map(f, htmls)



        
