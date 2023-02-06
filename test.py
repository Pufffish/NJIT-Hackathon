import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

baseurl = "https://www.rei.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

k = requests.get('https://www.rei.com/c/camping-and-hiking?ir=category%3Acamping-and-hiking&pagesize=90').text
soup=BeautifulSoup(k,'html.parser')
productlist = soup.find_all("li",{"class":"pPe0GNuagvmEFURs1Q_vm"})
print(productlist)


productlinks = []
for product in productlist:
    link = product.find("a",{"class":"_1A-arB0CEJjk5iTZIRpjPs _1K5N3WSl_8ywawYr0tzSgT"}).get('href')
    productlinks.append(baseurl + link)

productlinks = []
for x in range(1,8):  
 k = requests.get('https://www.rei.com/c/camping-and-hiking?ir=category%3Acamping-and-hiking&pagesize=90'.format(x)).text  
 soup=BeautifulSoup(k,'html.parser')  
 productlist = soup.find_all("li",{"class":"pPe0GNuagvmEFURs1Q_vm"})

for product in productlist:
    link = product.find("a",{"class":"_1A-arB0CEJjk5iTZIRpjPs _1K5N3WSl_8ywawYr0tzSgT"}).get('href')
    productlinks.append(baseurl + link)

data=[]
for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("span",{"id":"buy-box-product-price"}).text.replace('\n',"")
    except:
        price = None

    try:
        rating = hun.find("span",{"class":"cdr-rating__number_11-3-1"}).text.replace('\n',"")
    except:
        rating=None

    try:
        name=hun.find("h1",{"id":"product-page-title"}).text.replace('\n',"")
    except:
        name=None

    camp = {"Name":name,"Price":price,"Rating":rating}

    data.append(camp)

df = pd.DataFrame(data)

# print(df)

df.to_csv('df.csv', encoding='utf-8')

a = pd.read_csv("df.csv")

a.to_html("Prices.html")
 
html_file = a.to_html()