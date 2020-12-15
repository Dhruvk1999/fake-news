'''for scarping page on moneycontrol.com stock section '''
import bs4,requests
  
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
