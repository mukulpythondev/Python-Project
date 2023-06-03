from bs4 import BeautifulSoup
import pandas as pd
import requests
url='https://www.iplt20.com/auction/2022'
r=requests.get(url)
soup=BeautifulSoup(r.text, 'lxml')
#print(soup)
table=soup.find('table', class_="ih-td-tab auction-tbl")
title=table.find_all('th')# gettting table fields 
lst=[]
for i in title:
    entry=i.text
    lst.append(entry)
#print(lst)
df=pd.DataFrame(columns=lst)
#print(df)
data=table.find_all('tr')
#print(data)
for i in data[1:]:
    first_td=i.find_all('td')[0].find('div', class_='ih-pt-ic').text.strip()
    row=i.find_all('td')[1:]
    td=[tr.text for tr in row]
    td.insert(0, first_td)
    l=len(df)
    df.loc[l]=td
print(df)
df.to_csv('Ipl auction stats 2023.csv')# saving the scraped data in csv file 
