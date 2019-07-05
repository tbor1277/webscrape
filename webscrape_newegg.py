#!python3

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_Url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

uClient = uReq(my_Url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
    title_container = container.find("a", {"class":"item-title"})
    title = title_container.text
    price_container = container.find("li",{"class":"price-current"})
    price_text = price_container.text
    priceRegex = re.compile(r'[\$]{1}[\d,]+\.?\d{0,2}')
    price = priceRegex.findall(price_text)
    print('Product name: ' + str(title))
    print('Price: ' + str(price[0]))
