import requests
import json
import time
from selenium import webdriver

print("Hello I am a monitor bot written in python")
#allows you to access website information

def product_list():
    r = requests.get('https://kith.com/products.json')
    products = json.loads((r.text))['products']

    for product in products:
        productname = product['title'] 
        print (productname)

#check stock function
def avaliable_stock():
    r = requests.get('https://kith.com/products.json')
    products = json.loads((r.text))['products']
    for product in products:
        productname = product['title']
        if productname == text: 
            print ("\nProduct "+ product['title'] +" in stock\n ") 
            product_url = 'https://kith.com/products/' + product['handle']
            return (product_url)
    else: 
        return False

product_list()

text = input("what product are you looking to check: ")
new_url = avaliable_stock()

#loop to continuously check stock
while True:
    if new_url != False:
        print(new_url + '\n')
        break
    else:
        print('not avaliable')