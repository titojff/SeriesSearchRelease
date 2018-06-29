#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import html5lib






html = requests.get("https://www.imdb.com/title/tt5114356/episodes?season=1").content
soup = BeautifulSoup(html, 'html5lib')

tex=soup.text
a=tex.find("Year")
b=tex.find(",", a)
b=b+9

print (ord(tex[b]))
while (tex[b]==" "or tex[b]==chr(10)):
	b=b+1	
#while LF ou " " 2 seguidos fim de data	
print(b)	
print (tex[(b):(b+11)])

 
