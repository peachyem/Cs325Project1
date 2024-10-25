#importing all required libraries
import requests
from bs4 import BeautifulSoup

def get_reviews(url, page):
    headers = {'User-Agent' : 'Mozilla/5.0'}                #Helps pass information to a website more easily
    url +=str(page)                                         #adds the page number to the url
    r = requests.get(url, headers=headers, timeout=10)      #sends request to pull the url
    r.raise_for_status()                                    #raises an error if something does not pull properly
    return r

#this function calls Beautiful Soup to parse the data from the url passed in
#then finds all reviews in the pre-white-space class, which is the html where the reviews are stored
def parse(data): 
    soup = BeautifulSoup(data.text, 'html.parser')   
    all_reviews = soup.find_all(class_="pre-white-space")
    return all_reviews

#this function opens the file passed into it and then appends the current review to the file and then goes to a new line
def write_to_file(all_reviews, filename):                               
    with open(filename, 'a', encoding='utf-8') as reviewsfile:
        for reviews in all_reviews:
            reviewsfile.write(reviews.get_text(strip=True) + '\n')      
    return

def main():
    page = 1                                            #a way to move to next url
    with open('urls.txt', 'r') as file:                 #opens url file
        urls = file.readlines()                         #saves every url to a list

    count = 6                                           #count starts at 6 because we start at the 6th gen ipad
    for url in urls:                                    #increments for all urls
        url.strip()                                     #removes white space from url
        while(page < 7):                                #chose 7 because it will pull around 140 reviews
            data = get_reviews(url, page)               #calls the get_reviews function and saves it to a variable
            review = parse(data)                        #calls the parse function and saves it to a variable
            filename = 'ipad'+str(count)+'.txt'         #saves the current file to output reviews to
            write_to_file(review, filename)
            page +=1                                    #incrementing page to get more reviews

        page = 1                                        #resetting page counter
        count +=1                                       #incrementing count to move to next text file

main()                                                  #calling main function