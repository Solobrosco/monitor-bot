import requests
import json

print("Hello I am a monitor bot written in python");
#allows you to access website information
r = requests.get('https://kith.com/products.json')
products = json.loads((r.text))['products']
#print(products)

for product in products:
    productname = product['title']
    print(productname)

#print(products[1])
#used raw_input instead of input 
text = raw_input("what product are you looking to check: ") 

     
if (productname.find(text)!= -1): 
    print ("\nProduct "+text+" in stock\n ") 
else: 
    print ("Product does not exist")
