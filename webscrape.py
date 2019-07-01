#!python3

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_Url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opening up connection, grabbing the page
uClient = uReq(my_Url)
page_html = uClient.read()
uClient.close()

# html parsing-analyze (a string or text) into logical
# syntactic components, typically in order to test conformability
# to a logical grammar.
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})


# start of the for loop
for container in containers:
    title_container = container.find("a", {"class":"item-title"})
    title = title_container.text

    price_container = container.find("li",{"class":"price-current"})
    price_text = price_container.text
    priceRegex = re.compile(r'[\$]{1}[\d,]+\.?\d{0,2}')
    price = priceRegex.findall(price_text)

    print('Product name: ' + str(title))
    print('Price: ' + str(price[0]))
