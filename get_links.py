import requests
import random
from bs4 import BeautifulSoup

def save_the_link():
    url = f'https://www.rawpixel.com/search/background?page={random.randint(1,10)}&sort=curated'
    r = requests.get(url,'html.parser')
    soup = BeautifulSoup(r.content, 'html5lib')
    link = []
    imgs = soup.findAll('link')
    for img in imgs:
        lnk = img.get('href')
        link.append(lnk+'\n')
    with open('link.txt','w') as f:
        f.writelines(link)
    return 