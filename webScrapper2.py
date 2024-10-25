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
ipad6 = 'ipad6.txt'
ipad7 = 'ipad7.txt'
ipad8 = 'ipad8.txt'
ipad9 = 'ipad9.txt'
ipad10 = 'ipad10.txt'

url6 = "https://www.bestbuy.com/site/reviews/apple-certified-refurbished-ipad-6th-generation-2018-wi-fi-32gb-silver/6434298?variant=A&page="
url7 = "https://www.bestbuy.com/site/reviews/apple-geek-squad-certified-refurbished-10-2-inch-ipad-7th-generation-with-wi-fi-32gb-gold/6482000?variant=A&page="
url8 = "https://www.bestbuy.com/site/reviews/apple-geek-squad-certified-refurbished-10-2-inch-ipad-8th-generation-with-wi-fi-32gb-gold/6482863?variant=A&page="
url9 = "https://www.bestbuy.com/site/reviews/apple-10-2-inch-ipad-9th-generation-with-wi-fi-64gb-space-gray/4901809?variant=A&page="
url10 = "https://www.bestbuy.com/site/reviews/apple-10-9-inch-ipad-latest-model-10th-generation-with-wi-fi-64gb-yellow/5200906?variant=A&page="

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

def main(url, currentpage, filename):
    page = 1
    while(currentpage < 7):
        data = get_reviews(url, page)
        review = parse(data)
        write_to_file(review, filename)
        currentpage += 1
        page +=1
        print("scrapping!")

main(url6, currentpage, ipad6)
main(url7, currentpage, ipad7)
main(url8, currentpage, ipad8)
main(url9, currentpage, ipad9)
main(url10, currentpage, ipad10)