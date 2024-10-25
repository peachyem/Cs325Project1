#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

currentpage = 1
totalpage = 1
#test to see if it is being scrapped
#print("Currently Scraping page: "+str(current_page))
#url for a website
#ipad6 = 'ipad6.txt'
#ipad7 = 'ipad7.txt'
#ipad8 = 'ipad8.txt'
#ipad9 = 'ipad9.txt'
#ipad10 = 'ipad10.txt'

def get_reviews(url, page):
    headers = {'User-Agent' : 'Mozilla/5.0'}
    url +=str(page)
    r = requests.get(url, headers=headers, timeout=10)   #sends request to pull the url
    r.raise_for_status()
    #url = url[:-1]
    return r

def parse(data):
    soup = BeautifulSoup(data.text, 'html.parser')   #calls Beautiful Soup to parse the data
    all_reviews = soup.find_all(class_="pre-white-space")
    return all_reviews

def write_to_file(all_reviews, filename):
    with open(filename, 'a', encoding='utf-8') as reviewsfile:
        for reviews in all_reviews:
            reviewsfile.write(reviews.get_text(strip=True) + '\n')
    return

def main(currentpage):
    page = 1
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
    print(urls)    
    count = 6
    for url in urls:
        url.strip()
        while(page < 7):
            print(url)
            data = get_reviews(url, page)
            review = parse(data)
            filename = 'ipad'+str(count)+'.txt'
            print(filename)
            write_to_file(review, filename)
            currentpage += 1
            page +=1
            print("scrapping!")
        page = 1
        count +=1

main(currentpage)