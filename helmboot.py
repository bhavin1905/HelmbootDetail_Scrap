import requests 
import json
import pandas as pd

url = 'https://helmboots.com/products.json'

r = requests.get(url)

data = r.json()

product_list = []

for item in data['products']:
    title = item['title']
    handle = item['handle']
    created = item['created_at']
    product_type = item['product_type']
    # print(title, handle, created, product_type)

    for variant in item['variants']:
        sku = variant['sku']
        taxable = variant['taxable']
        price = variant['price']
        available = variant['available']
        grams = variant['grams']
    
    for image in item['images']:
        try:
            src = image['src']
        except:
            'None'
        
        product = {
            'title': title,
            'handle': handle,
            'created': created,
            'product_type': product_type,
            'sku': sku,
            'taxable': taxable,
            'price': price,
            'available': available,
            'grams': grams,
            'src': src,
        }
        product_list.append(product)
    
df = pd.DataFrame(product_list)

df.to_csv('tryjson.csv')