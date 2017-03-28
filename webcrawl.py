import urllib2

url = 'http://nj.gov/governor/news/news/552017/approved/20170324b.html'
r = urllib2.urlopen(url).read() 
#f = open('new.html', 'w')
#f.writelines(page)
#f.close()

from bs4 import BeautifulSoup
soup = BeautifulSoup(r,  "lxml")
#print soup.prettify()[0:1000]
#print soup.getText()

# conda install -c conda-forge jpype1
# pip install charade
# pip install boilerpipe

from boilerpipe.extract import Extractor
extractor = Extractor(extractor='ArticleExtractor', url= url)
print extractor.getText()
