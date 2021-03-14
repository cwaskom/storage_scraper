import requests
from datetime import datetime
from bs4 import BeautifulSoup
# from models import db, RateModel
import time

# headers
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# URL to scrape
URL = 'https://www.extraspace.com/storage/facilities/us/connecticut/groton/320221/'

# requests page
def scrape(URL, headers):
    page = requests.get(URL, headers)
    print(page.status_code)
    return page

# parse html
def parse(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='displayUnits')
    try:
        unit_elems = results.find_all('div', class_='unit-row')
    except:
        time.sleep(2) 
        unit_elems = results.find_all('div', class_='unit-row')
    return unit_elems

# check if units are available
def check_availabilty(unit_elem):
    if unit_elem.find('div', class_="makes-offer").find('div', class_="rate").get_text()[0] != "$":
        return False
    else:
        return True

# clean and create list of dictionaries of units
def clean_and_load(unit_elems):
    data_list = []
    for unit_elem in unit_elems:
        data = {}
        data["name"] = "Extra Space"
        data["market"] = "Groton"
        data["size"] = unit_elem.find('div')['data-dimensions']
        data["rate"] = unit_elem.find('div')['data-website']
        data["features"] = unit_elem.find('div', class_='features').get_text(separator=', ')
        data["avail"] = check_availabilty(unit_elem)
        data_list.append(data)
    return data_list
 

# if __name__ == "__main__":
def run_scraper():
    page = scrape(URL, headers)
    unit_elems = parse(page)
    data = clean_and_load(unit_elems)