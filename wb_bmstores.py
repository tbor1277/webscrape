#!bin/env/python3

from bs4 import BeautifulSoup as soup
import requests

def simple_get(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error: %s' % (exc))
    else:
        return soup(res.text, 'html.parser')

def link_merge(link_two):
    half_link = link_two
    return main_site + half_link[7:]


main_site = 'https://www.bmstores.co.uk/stores'
html_page = simple_get(main_site)
columns = html_page.find_all("div", {"class": "col-xs-4"})
county_list = []
second_site_list = []
for column in columns[0:3]:
    counties = column.text.split('\n')
    for county in counties[1: len(counties) - 1]:
        county_name = county
        county_list = county_list + [county_name]
    for a in column.find_all('a', href=True):
        second_site = link_merge(a["href"])
        second_site_list = second_site_list + [second_site]


print('Merging lists...')
county_link_list = dict(zip(county_list, second_site_list))
for county in county_list:
    print('County Name: ' + county)
    county_link = county_link_list[county]
    print('County Link: ' + county_link)
    second_html_page = simple_get(county_link)
    containers = second_html_page.find_all("th", {"style": "width: 50%;"})
    for container in containers:
        for link in container.find_all('a'):
            third_site = link_merge(link.get('href'))
            third_html_page = simple_get(third_site)
            store_address = third_html_page.address.text
            print('Store Adress: ' + store_address) 
            print('Store link: ' + third_site)
