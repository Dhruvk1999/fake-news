'''for scarping pages on moneycontrol.com stock section'''
import bs4,requests
import re
  
headlines=[]   
        
j='https://www.moneycontrol.com/news/business/stocks/'
res=requests.get(j)


res.raise_for_status()
text=bs4.BeautifulSoup(res.text)
heads=text.find_all('div',attrs={'id':'left'})
for a in heads:
    links=a.find_all('a')
k=[]
for link in links:
    l=link.get_text()
    k.append(l)
 
for hl in k:
    if len(hl)>25:
        headlines.append(hl)    
        

def tip_filter(headline):
    headline=headline.lower()
    if 'buy' in headline:
        return headline
    elif 'sell' in headline:
        return headline
    elif  'hold' in headline:
        return headline
    elif  'accumulate' in headline:
        return headline
    elif  'target' in headline:
        return headline
    else: 
        pass
    
tips=list(filter(tip_filter,headlines))