import urllib.request
import datetime
from bs4 import BeautifulSoup
import csv
quote_page = "https://www.bakingo.com/cake-delivery"
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

csv_file=open('scraped.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Product_ID','links','title','short_title','price','description','Date_Time'])

img_list=[]
tit_list=[]
s_tit_list=[]
p_list=[]
des_list=[]
pid=[]



print('**************************************************')





for b in soup.find_all("div",{'class':'cake-img'}):
    for a in b.find_all('img',src=True):
        print ("Found the URL:", a['src'])
        links=a['src']
        
        #csv_writer.writerow([links])
        img_list=img_list+[links]

i=1
for c in soup.find_all("div",{'class':'cake-title'}):
    #print ("Found the URL:",b.text.strip())
    title=c.text.strip()
    tit_list=tit_list+[title]
    pid=pid+[i]
    i=i+1
    #csv_writer.writerow([links,title])


for e in soup.find_all("div",{'class':'cake-pd'}):
    #print ("Found the URL:",b.text)
    s_tit=e.text
    #csv_writer.writerow([links])
    s_tit_list=s_tit_list+[s_tit]

    
for f in soup.find_all("div",{'class':'cake-p'}):
    #print ("Found the URL:",b.text)
    price=f.text
    #csv_writer.writerow([links])
    p_list=p_list+[price]
dttm=[]
for g in soup.find_all("div",{'class':'cake-desc'}):
    #print ("Found the URL:",b.text)
    des=g.text.strip()
    #csv_writer.writerow([links])
    des_list=des_list+[des]
    dttm=dttm+[datetime.datetime.now()]





'''for d in dttm:
    dttm=dttm+[datetime.datetime.now()];'''
    

zipped=zip(pid,img_list,tit_list,s_tit_list,p_list,des_list,dttm)
d=list(zipped)#list of lists
print(d)
csv_writer.writerows(d)
csv_file.close()


