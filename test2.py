import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

baseurl = "https://www.rei.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

k = requests.get('https://www.rei.com/c/camping-and-hiking').text
soup=BeautifulSoup(k,'html.parser')
productlist = soup.find_all("li",{"class":"pPe0GNuagvmEFURs1Q_vm"})
print(productlist)

# for product in productlist:
#     link = product.find("a",{"class":"_1A-arB0CEJjk5iTZIRpjPs _1K5N3WSl_8ywawYr0tzSgT"}).get('href')
#     productlinks.append(baseurl + link)

# productlinks = []
# for x in range(1,140):  
#  k = requests.get('https://www.rei.com/c/camping-and-hiking'.format(x)).text  
#  soup=BeautifulSoup(k,'html.parser')  
#  productlist = soup.find_all("li",{"class":"pPe0GNuagvmEFURs1Q_vm"})
 
# for product in productlist:
#     link = product.find("a",{"class":"_1A-arB0CEJjk5iTZIRpjPs _1K5N3WSl_8ywawYr0tzSgT"}).get('href')
#     productlinks.append(baseurl + link)

productlinks = 'https://www.rei.com/c/camping-and-hiking'
pages = 3
data=[]


# goal is to go from original link (productLinks https://www.rei.com/c/camping-and-hiking) to https://www.rei.com/c/camping-and-hiking?page=139

f = requests.get(productlinks).text
hun=BeautifulSoup(f,'html.parser')

try:
    price=hun.find("span",{"data-ui":"sale-price"}).text.replace('\n',"")
except:
    price = None

try:
    rating = hun.find("span",{"class":"cdr-rating__caption-sr_11-1-0"}).text.replace('\n',"")
except:
    rating=None

try:
    name=hun.find("span",{"data-ui":"product-title"}).text.replace('\n',"")
except:
    name=None

camp = {"name":name,"price":price,"rating":rating}

data.append(camp)

df = pd.DataFrame(data)

print(df)