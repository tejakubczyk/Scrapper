import selenium as sel
from bs4 import BeautifulSoup #parser - analizator składniowy
import pandas as pd
import requests as req

#page = '''<a href="https://onet.pl">next</a>'''
page = req.get("https://upwr.edu.pl")
#print(page.content)
soup = BeautifulSoup(page.text, "html.parser")

for link in soup.find_all("a", href=True):
    if link.get('href')[0] != "/" and link.get('href')[0] != "#":
        print(f"Found an URL: {link.get('href')}")
