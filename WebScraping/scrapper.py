#This is a web scrapping project
import requests
from bs4 import BeautifulSoup
url='https://www.codewithharry.com'
# Step 1: Get The HTML 
r=requests.get(url)
htmlContent = r.content
# print(htmlContent)
# Step 2: Parse the HTML
soup=BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)
# Step 3:HTML Tree Traversal  
#commonly used objects
#1.tags
# print(type(title))
#2. beautifulsoup
# print(type(soup))
#3.comments
# markup="<p> <-- this is a comment--></p>"
# soup2=BeautifulSoup(markup)
# print(soup2)


#4. Navigable String
# print(type(title.String))
#get title of html page
title=soup.title
#get all paragraph of page
para=soup.find_all('p')
# to get anchor tags
anchor=soup.find_all('a')
all_links=set()
# get links on the page
for link in anchor:
    id (link !='#')
    all_links.add('https://www.codewithharry.com'+link.get('href'))
    print(all_links)
#print(anchor)
# get the first element of HTML
# print(soup.find('p'))
# print(soup.find('p')['class'])
# to get all the elements  with class lead
#print(soup.find_all('p', class_='lead'))

# get the text from the tags/soup
print(soup.find('p').get_text())

navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)

 



