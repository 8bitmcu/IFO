import urllib2
from bs4 import BeautifulSoup

import time
from time import mktime
from datetime import datetime

## scrape Hackaday
print "---  HACK A DAY  ----"
soup = BeautifulSoup(urllib2.urlopen('http://hackaday.com/').read())

content = soup.findAll('div', 'post')

for x in content:
  #print x

  if(x.find('span', 'date')):
    ## title
    print x.find('h2').a.string

    ## date
    print x.find('span', 'date')['title']

    ## link
    #print x.find('h2').a['href']

    ## image url
    #print x.find('img')['src']

    ## description
    #for p in x.find('div', 'entry-content').findAll('p'):
      #for e in p.contents:
        
        #print e
        #print "///"
      #print p.string
    #print
    #print "----------------"
    print 

## scrape HackerNews
soup = BeautifulSoup(urllib2.urlopen('http://news.ycombinator.com/').read())
print "--- HACKER NEWS ---"
content = soup.table.findAll('tr')

for x in content:
  article = x.findAll('td', 'title')

  if(len(article) > 1):

    ## title
    print article[1].find('a').string

    ## link
    #print article[1].find('a')['href']

    ## votes
    votes = x.nextSibling.find('span')
    if(votes):
      print votes.string
    print


## scrape news 91.9
soup = BeautifulSoup(urllib2.urlopen('http://www.news919.com/category/news/local/').read())
print "--- NEWS 91.9 ----"
content = soup.h3.findNextSibling('div').findAll('li')

for x in content:
  ## title
  print "[" + x.find('h4').a.string + "]"

  ## short description
  #print x.findAll('p')[1].string

  ## time
  #print x.find('time')['datetime']

  ## linkto
  url =  x.find('a')['href']
  #print url

  ## long description
  linkData = BeautifulSoup(urllib2.urlopen(url).read())

  for p in linkData.find('div', 'post-content').findAll('p'):
    if(p.string):
      print "  " + p.string
  print

  ## image url
  #print linkData.find('img', 'attachment-spotlight-image').parent['href']


## Scrape Tidal Wave (Moncton)
soup = BeautifulSoup(urllib2.urlopen('http://www.waterlevels.gc.ca/eng/station?sid=175&tz=AST&pres=2').read())
print "--- TIDAL WAVE ----"
content = soup.find('div', 'stationTextData')

#next waves
for div in content:
  print div.string.strip()

## time until next wave
## get the time of the first item of the list
t = content.div.string.strip()
## parse timeformat: 2013/02/21;6:42 AM
t = time.strptime(t, "%Y/%m/%d;%I:%M %p")
#print

## time until next wave
print datetime.fromtimestamp(mktime(t)) - datetime.now()






## Scrape Deal Extreme
soup = BeautifulSoup(urllib2.urlopen('http://dx.com/new-arrivals?pageSize=100').read())
print "--- DEAL EXTREME ----"
content = soup.find('div', 'cate_mainbox').find('ul', 'productList').findAll('li')

for li in content:
  ## item name
  print li.find('p', 'title').a.string

  ## item url
  #print "http://dx.com" + li.find('p', 'title').a['href']

  ## item price
  print li.find('p', 'price').string.strip()

  ## hidden desc
  #print li.find('p', 'des').string

  ## thumbnail
  #print "http://dx.com" + li.find('img', 'lazy')['data-src']

  print








## Scrape weather radar
soup = BeautifulSoup(urllib2.urlopen('http://www.weatheroffice.gc.ca/radar/index_e.html?id=XNC').read())
print "--- WEATHER RADAR ----"
content = soup.find('div', 'image list').findAll('a')

for li in content:

  ## image path
  print "http://www.weatheroffice.gc.ca" + li['href'].split('display=')[1]