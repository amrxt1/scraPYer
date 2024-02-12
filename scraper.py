import requests
from bs4 import BeautifulSoup
import os
import smtplib
import time

def check_price():
    URL = 'https://www.amazon.in/Indus-Valley-Super-Smooth-Cast/dp/B0CQ4NKWVD?ref_=Oct_DLandingS_D_a062a2b8_0'

    h = {"User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

    page = requests.get(URL, headers=h)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = int(soup.find('span', class_='a-price-whole').get_text()[:-1].replace(',',''))
    print(price)

    if price>1000:
        mailer()

def mailer():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(os.environ["MAIL"], os.environ["SCRAPER_PASS"])
    subject = "PRICE DROPPED!"
    body = 'The price has dropeed. Go to: https://www.amazon.in/Indus-Valley-Super-Smooth-Cast/dp/B0CQ4NKWVD?ref_=Oct_DLandingS_D_a062a2b8_0'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        os.environ["MAIL"],
        'amritveer638@gmail.com',
        msg
    )

    print("Email HAS BEEN SENT")
    server.quit()

while True:
    check_price()
    time.sleep(3)