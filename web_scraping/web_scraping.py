import requests
from bs4 import BeautifulSoup
import urllib



if __name__ == '__main__':
    for i in range(1,10):
        response = requests.get('https://xkcd.com/{}/'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        img_cont = soup.find(id='comic')
        img_file = img_cont.find('img')['src']
        img_name = img_file.split('/')[-1]
        urllib.request.urlretrieve('https:{}'.format(img_file), img_name)