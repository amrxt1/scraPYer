import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Indus-Valley-Super-Smooth-Cast/dp/B0CQ4NKWVD?ref_=Oct_DLandingS_D_a062a2b8_0'

h = {"User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=h)

soup = BeautifulSoup(page.content, 'html.parser')

jobs = int(soup.find('span', class_='a-price-whole').get_text()[:-1].replace(',',''))

print(jobs)