#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#saving the data and opening the file we will write to
data = []
current_page = 1
reviewfile = open('reviews1.txt', 'w')
#loop condition
proceed = True

while(proceed):
    #test to see if it is being scrapped
    print("Currently Scraping page: "+str(current_page))
    #url for a website
    url = "https://store.steampowered.com/app/504230/Celeste/"

    #where we are pulling the page cite html
    page = requests.get(url)


    soup = BeautifulSoup(page.text, "html.parser")

    #printing to see if we are actually connecting
    print(page.text)
    if current_page == 50:
        proceed = False
    else:
        #finds the section of html that each review is encased in
        all_reviews = soup.find_all("div",class_="review_box    partial")

        for review in all_reviews:
            item = {}
            #pulls the review by checking if the type and class match
            item['Review'] = review.find("div",class_="content")
            string = " ".join(item['Review'])
            #data.append(item)
            reviewfile.write(string)

    #increments the page number
    current_page += 1
    proceed = False
