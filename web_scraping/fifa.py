from typing import TextIO

import requests
import json

if __name__ == '__main__':
    url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page="
    r = requests.get(url + '1')
    items = []
    if r is not None:
        cont = r.json()
        if cont is not None:
            pages = int(cont['totalPages'])
            for page in range(1, pages + 1):
                r = requests.get(url + '1')
                result = r.json()
                items += result['items']
                
                
                
            with open('fifa/items/fifa.items.json', 'w') as outfile:
                json.dump(items, outfile)
                outfile.close()
