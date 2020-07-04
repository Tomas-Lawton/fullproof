# Navid-S-B
# 3-07-2020
"""
Webscraping script to access Google RIS using API Key to gather extra but  
important content not obtainable through the JSON file from the API.
"""

from bs4 import BeautifulSoup
from urllib import request
import re

class serpapi_webpage:

    # Adjust link given
    def __init__(self, image_url):
        
        self.image_url = image_url
        self.api_key = "insert_api_key"
        # Editing link given in for webpage search using REGEX
        p = re.compile('/')
        self.new_url = p.sub("%2F", self.image_url)
        p = re.compile(':')
        self.new_url = p.sub("%3A", self.new_url)
        self.new_url = "https://serpapi.com/search.html?engine=google_reverse_image&image_url={}&&api_key={}".format(self.new_url, self.api_key)
    
    def get_no_total_results(self):

        # Get webpage
        response = request.urlopen(self.new_url).read()
        soup = BeautifulSoup(response,'lxml')
        # Gather html code containing number of searches
        result = str(soup.find(id = 'result-stats'))
        # Use REGEX to modify string into returnable number
        p = re.compile('.+s">')
        result = p.sub("", result)
        p = re.compile('<nobr>.*')
        result = p.sub("", result)
        p = re.compile("[^0-9]")
        result = p.sub("", result)
        return int(result)
    
    def related_search_term(self):
        
        # Get webpage
        response = request.urlopen(self.new_url).read()
        soup = BeautifulSoup(response,'lxml')
        # Gather html code containing number of searches
        result = str(soup.find(class_ = 'fKDtNb'))
        # Use REGEX to get desirable string
        p = re.compile('.*italic">')
        result = p.sub("", result)
        p = re.compile('<.*')
        result = p.sub("", result)
        return result

"""
# Testing code, algorithm time varies, sometimes quick, sometimes not (~4s).
# Minor optimisations maybe required, or the server has slowed down.
# Could add this on with TinEye as an option since TinEye does not have
# this particular functionality.

test_link = None
time_1 = time.perf_counter()
extra_image_info = scrape_webpage('https://i0.wp.com/metro.co.uk/wp-content/uploads/2019/09/PRI_85898263.jpg?quality=90&strip=all&zoom=1&resize=644%2C475&ssl=1')
print(extra_image_info.related_search_term())
print(extra_image_info.get_no_total_results())
time_2 = time.perf_counter()
print(time_2-time_1)
"""