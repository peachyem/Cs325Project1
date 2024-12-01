import requests
import ollama
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

numiPads = 5

class FileHandler:                                                                          #Parent Class
    def __init__(self, fileName):                                                           #saves filename to class instance
        self.fileName = fileName
    def open_read_file(self):                                                               #opens a file to be read
        with open(self.fileName, 'r', encoding = 'utf-8') as file:
            revs = file.readlines()                                                         #reads every line in file and stores it in a variable
        return revs                                                                         #returns the variable
    def open_write_file(self):                                                              #opens a write file
        return open(self.fileName, 'w')
    def write_file(self, text):                                                             #writes to the specified file
        self.fileName.write(text)
    def close_file(self):                                                                   #closes the specified file
        file = self.fileName
        file.close()
    
class UrlFile(FileHandler):                                                                 #inherits from FileHandler Class
    def __init__(self, fileName):                                                           #saves filename to class instance
        self.fileName = fileName

    def open_file(self):
        with open(self.fileName, 'r') as file:                                              #opens url file
            urls = file.readlines()                                                         #saves every url to a list
        return urls                                                                         #returns the list
   
    def write_file(self, file, text):
        with open(file, 'a', encoding = 'utf-8') as filename:
            for reviews in text:                                                            #iterates through reviews in class for the text passed in
                filename.write(reviews.get_text(strip=True) + '\n')                         #writes review to file passed in

class Response():
    def __init__(self, review):                                                             #saves the review to the instance of the class
        self.review = review
    def prompt(self):
        return ollama.generate(model="phi3:mini", prompt=self.review)                       #prompts ollama with the review and returns the response
    def cleanResponse(self, res):
        clean = res["response"] + '\n'                                                      #returns only the response from ollama
        return clean
  
class WebScrapper:
    def __init__(self, url, page):                                                          #saves the url and page to the instance of the class
        self.url = url
        self.page = page

    def get_reviews(self):
        headers = {'User-Agent' : 'Mozilla/5.0'}                                            #Helps pass information to a website more easily
        self.url +=str(self.page)                                                           #adds the page number to the url
        r = requests.get(self.url, headers=headers, timeout=120)                            #sends request to pull the url
        r.raise_for_status()                                                                #raises an error if something does not pull properly
        return r
    
    def parse(self, data):                                                                  #this function calls Beautiful Soup to parse the data from the url passed in
        soup = BeautifulSoup(data.text, 'html.parser')                                      #then finds all reviews in the pre-white-space class, which is the html where the reviews are stored
        all_reviews = soup.find_all(class_="pre-white-space")
        return all_reviews



def find_numbers(filename):                                                                 #finds the number of positive, nuetral, and negative reviews
    file = open(filename, 'r', encoding = 'utf-8')                                          #opens the file passed in
    lines = file.readlines()                                                                #reads every line of the file
    pos = 0                                                                                 #initializes the variables to 0 on every call
    neg = 0
    nue = 0
    for row in lines:                                                                       #iterates for the number of lines in the file
        if row.find("Positive") != -1 or row.find("positive") != -1:                        #checks if the word is found on the current row, if it is add 1 to the total
            pos = pos + 1
        if row.find("Nuetral") != -1 or row.find("nuetral") != -1:
            nue += 1
        if row.find("Negative") != -1 or row.find("negative") != -1:
            neg += 1
    return pos, neg, nue                                                                    #return the variables
        
def make_graph():                                                                           #creates the clustered column chart
    devices = ("iPad 6", "iPad 7", "iPad 8", "iPad 9", "iPad 10")                           #saves the name of the devices
    pos6, neg6, nue6 = find_numbers('responses6.txt')                                       #calling the find_numnbers function on all response files
    pos7, neg7, nue7 = find_numbers('responses7.txt')
    pos8, neg8, nue8 = find_numbers('responses8.txt')
    pos9, neg9, nue9 = find_numbers('responses9.txt')
    pos10, neg10, nue10 = find_numbers('responses10.txt')

    iPad_data = {                                                                           #saves the iPad data to their respective types
        'Positive' : (pos6, pos7, pos8, pos9, pos10),
        'Nuetral' : (nue6, nue7, nue8, nue9, nue10),
        'Negative' : (neg6, neg7, neg8, neg9, neg10),
    }

    x = np.arange(len(devices))                                                             #aranges the data by the number of devices
    width = 0.25                                                                            #specifies width
    multiplier = 0                                                                          #creates a multiplier variable

    fig, ax = plt.subplots(layout='constrained')                                            #creates the matplot variable

    for attribute, measurement in iPad_data.items():                                        #for every item in iPad_data
        offset = width * multiplier                                                         #specifies offest
        rects = ax.bar(x + offset, measurement, width, label=attribute)                     #gives specifices for the bar presentation
        ax.bar_label(rects, padding = 3)                                                    #specifices the label
        multiplier += 1                                                                     #increase multiplier
    
    ax.set_ylabel('Num Reviews')                                                            #set the ylabel for the chart
    ax.set_title('iPad Reviews')                                                            #set the title for the reviews
    ax.set_xticks(x+width, devices)                                                         #sets the width for the bars
    ax.legend(loc='upper left', ncols=3)                                                    #specifies where to put the legend
    ax.set_ylim(0,200)                                                                      #sets the limits for the y-aixs
    plt.show()                                                                              #shows the plot




def main():
    page = 1
    count = 6                                                                               #count starts at 6 because we start at the 6th gen ipad
    ur = UrlFile('urls.txt')
    urls = ur.open_file()

    for url in urls:                                                                        #increments for all urls
        url.strip()                                                                         #removes white space from url
        while(page < 3):                                                                    #the number of pages to pull the reviews from
            rev = WebScrapper(url, page)                                                    #creates an instance of the WebScrapper Class
            data = rev.get_reviews()                                                        #calls the get_reviews function and saves it to a variable
            review = rev.parse(data)                                                        #calls the parse function and saves it to a variable
            filename = 'ipad'+str(count)+'.txt'                                             #saves the current file to output reviews to
            ur.write_file(filename, review)                                                 #saves the review to the current file
            page += 1                                                                       #incrementing page to get more reviews
        page = 1                                                                            #resetting page counter
        count +=1                                                                           #incrementing count to move to next text file
    count = 6                                                                               #resetting the counter
    

    while(count < 11 ):                                                                     #increments for iPads 6 - 10
        ipads = FileHandler('ipad'+str(count)+'.txt')                                       #creates a FileHandler instance of the current iPad
        reviews = ipads.open_read_file()                                                    #opens the iPad file as a read file
        responsefile = open('responses'+str(count)+'.txt', 'w', encoding = 'utf-8')         #opens a response file for ollama to write to
        for rev in reviews:                                                                 #increments for the number of reviews in the iPad file
            rev = "MESSAGE: Only respond with Positive, Nuetral or Negative. Can you please tell me if this is a Positive, Negative, or Nuetral review and only respond with one of the 3 options?" + str(rev)
            review = Response(rev)                                                          #creates an instance of the Response class
            prompt = review.prompt()                                                        #calls the prompt function
            clean = review.cleanResponse(prompt)                                            #calls the clean function
            responsefile.write(clean)                                                       #writes the clean data to the response file
        responsefile.close()                                                                #closes the response file
        count += 1                                                                          #increments count
    print("Time to make a graph")

    make_graph()                                                                            #calls the make_graph function

    
    

main()