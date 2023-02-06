###Imports###
#import to read url
import nltk
nltk.download()

import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
# import schedule
import urllib.request
import urllib
import string
import re 
from collections import Counter
from selenium import webdriver
import nltk
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}


driver = webdriver.Chrome()

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

nltk.download('stopwords')

stopword = stopwords.words('english'),('punctuation')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

#import to get information from the urls
link = "https://www.moosejaw.com/navigation/hiking-and-camping-gear"
driver.get(link)

###Reading information from websites
soup = BeautifulSoup(driver.page_source, 'html.parser')

products = soup.find_all(("div", {"class":"prod-item prod-item--three prod-item--two-tablet prod-item--one-mobile prod-item--bdb plp-search-item"})) # class for product 
print(len(products)) # number of products 

item = products[0]
print(item)


###Reading in information###

try:
   with urllib.request.urlopen('https://www.moosejaw.com/navigation/hiking-and-camping-gear') as f:
      print(f.read().decode('utf-8'))
except urllib.error.URLError as e:
   print(e.reason)

data = []
hun=BeautifulSoup(f,'html.parser')

try:
    price = hun.find("span",{"class":"price-option"}).text.replace('\n',"")
except:
    price = None

try:
    rating = hun.find("a",{"class":"prod-item__reviews"}).text.replace('\n',"")
except:
    rating = None

try:
    name = hun.find("a",{"class":"prod-item__name cf"}).text.replace('\n',"")
except:
    name = None

yeeyee = {"name":name,"price":price,"rating":rating}

data.append(yeeyee)

df = pd.DataFrame(data)

print(df)

with open('data.csv', 'a') as csv_file:
        writer_ETH = csv.writer(csv_file)
        writer_ETH.writerow([price, rating, name])

         
         
         
         

         


######## EXISTING CODE ###########

# import requests
# from bs4 import BeautifulSoup
# import csv
# from datetime import *
# import time
# import schedule

# def name_price():

#     #Bitcoin BTC 

#     # Website Address
#     BTC_Website = "https://coinmarketcap.com/currencies/bitcoin/"

#     #Sends server request to get its content and saves it in a HTML format
#     BTC_Info = BeautifulSoup(requests.get(BTC_Website).content, "html.parser")

#     #Finds the content under the header class 
#     BTC_Name = BTC_Info.find("h1", attrs={"class": "priceHeading"})

#     #Gets rid of spaces
#     BTC_finalName = BTC_Name.text.strip()

#     #Finds the fiv class and gets its value
#     price_box = BTC_Info.find("div", attrs={"class": "priceValue"})
    
#     #Saves the thing as text
#     price = price_box.text

#     now = datetime.now()
#     date_time = now.strftime("%m-%d-%Y")

#     with open('WebScraping\BTC.csv', 'a') as csv_file:
#         writer_BTC = csv.writer(csv_file)
#         writer_BTC.writerow([BTC_finalName, price, date_time])


##################EXISTING CODE FOR GETTING WIKIPEDIA STUFF MADE BY DHRUV##################

# import urllib.request
# import string
# from bs4 import BeautifulSoup
# import re 
# from collections import Counter

# wikilink = 'https://en.wikipedia.org/wiki/'

# #r = urllib.request.urlopen(wikilink)
# l = list(string.ascii_uppercase)

# for element1 in l:
#     for element2 in l:
#         # this is the actual url
#         urlvar = wikilink+element1+element2
#         # reads the url
#         link = urllib.request.urlopen(urlvar)
#         # print(urlvar)
#         data = link.read()
#         soup = BeautifulSoup(data, features = "lxml")
#         # print(soup.get_text())
#         # turn the html stuff into simple text
#         for element in soup(["script", "style"]):
#                 element.extract()
#         urltext = soup.get_text()
#         # print(urltext)
# counts =  Counter(re.findall('\w+', urltext))
# print(counts)
