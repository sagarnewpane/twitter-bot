import random
import requests

with open('link.txt','r') as f:
    s = f.readlines()
link = s[random.randint(60,len(s)-1)]

res=requests.get(str(link))


def save_img():
    with open('thumbnail.jpg','wb') as f:
            f.write(res.content)
            