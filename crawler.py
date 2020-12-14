'''for scarping pages on moneycontrol.com stock section'''
import bs4,requests
page_url="https://www.moneycontrol.com/news/business/stocks/page-"   
page_urls=[]
headlines=[]
for i in range(2,50):            #i is in range of page numbers to be scraped
    page_urls.append("https://www.moneycontrol.com/news/business/stocks/page-"+str(i))
    
        
for j in page_urls:
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