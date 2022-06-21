import requests
import random

url = 'https://type.fit/api/quotes'
response = requests.get(url)
quotes = response.json()

def get_quote():
    quote = quotes[random.randint(0,len(quotes)-1)]
    return quote['author'],quote['text']

