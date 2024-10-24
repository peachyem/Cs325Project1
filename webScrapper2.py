#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

currentpage = 1
#test to see if it is being scrapped
#print("Currently Scraping page: "+str(current_page))
#url for a website
url = "https://www.bestbuy.com/site/reviews/apple-macbook-air-13-inch-laptop-m3-chip-built-for-apple-intelligence-8gb-memory-256gb-ssd-midnight/6565837?variant=A&page="+str(currentpage)

def get_reviews(url):
    headers = {'User-Agent' : 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)   #sends request to pull the url
    r.raise_for_status()
    return r


def parse(data):
    soup = BeautifulSoup(data.text, 'html.parser')   #calls Beautiful Soup to parse the data
    all_reviews = soup.find_all(class_="pre-white-space")
    return all_reviews

def write_to_file(all_reviews):
    with open('reviews1.txt', 'w+', encoding='utf-8') as reviewsfile:
        for reviews in all_reviews:
            reviewsfile.write(reviews.get_text(strip=True) + '\n')
    return

data = get_reviews(url)
review = parse(data)
write_to_file(review)