import requests
import json
import time
from selenium import webdriver

print("Hello I am a monitor bot written in python");
#allows you to access website information

def product_list():
    r = requests.get('https://kith.com/products.json?limit=250')
    products = json.loads((r.text))['products']

    for product in products:
        productname = product['title'] 
        print (productname)

def avaliable_stock():
    r = requests.get('https://kith.com/products.json?limit=250')
    products = json.loads((r.text))['products']
    #print(products)
    #search by title
    for product in products:
        productname = product['title'] 

        if (productname.find(text)!= -1): 
            print ("\nProduct "+text+" in stock\n ") 
            if (text.find('WMNS')!= -1):
                product_url = 'https://kith.com/collections/womens-footwear/products/' + product['handle']
                return (product_url)

            else: 
                product_url = 'https://kith.com/collections/mens-footwear/products/' + product['handle']
                return (product_url)

        else: 
            return False

product_list()

text = raw_input("what product are you looking to check: ")
new_url = avaliable_stock()
if new_url != False:
    print (new_url + '\n')
else:
    print ('not avaliable')
#print(products[1])
#used raw_input instead of input 