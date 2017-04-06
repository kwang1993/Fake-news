from boilerpipe.extract import Extractor
from goose import Goose

def b(html):
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
    content = extractor.getText()
    print content 

##    - DefaultExtractor
##    - ArticleExtractor
##    - ArticleSentencesExtractor
##    - KeepEverythingExtractor
##    - KeepEverythingWithMinKWordsExtractor
##    - LargestContentExtractor
##    - NumWordsRulesExtractor
##    - CanolaExtractor


def g(html):
    print html
    txt = html + '.txt'        
    f = open(html, 'r')
    data = ''
    line = f.readline()
    while line:
        data += line
        line = f.readline()
    f.close()
    
    g = Goose()
    content = g.extract(raw_html = data)
    print content.cleaned_text
    
  

if __name__ == '__main__':
        #b('../new_0/1.html')
        #b('../new_6/10000.html')
        #g('../new_0/1.html')
        #g('../new_6/10000.html')


 
