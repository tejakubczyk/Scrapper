from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup #parser - analizator składniowy
import pandas as pd
import requests as req


bbc = req.get("https://www.bbc.com/news/technology")
soup = BeautifulSoup(bbc.text, "html.parser")
profile_path = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\y1uqp5mi.default'


print(soup.find('title').text)

texts = soup.find_all('p')
for text in texts:
    print(text.get_text())
