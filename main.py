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
            var = product['variants']
            #find available size
            for available in var:
                avail = available['available']
                size = available['title']
                if avail == True:
                    print (size + " -available")
            product_url = 'https://kith.com/products/' + product['handle']
            return (product_url)
    else: 
        return False

product_list()

text = input("what product are you looking to check: ")
#loop to continuously check stock
while True:
    new_url = avaliable_stock()
    if new_url != False:
        #driver = webdriver.Chrome(executable_path='/Users/aaronvanoung/Desktop/chromedriver')
        print(new_url + '\n')
        #driver.get(new_url)
        break
    else:
        print('not avaliable')
        time.sleep(1)