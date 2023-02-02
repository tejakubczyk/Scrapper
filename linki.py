import selenium as sel
from bs4 import BeautifulSoup #parser - analizator składniowy
import pandas as pd
import requests as req

#page = '''<a href="https://onet.pl">next</a>'''
page = req.get("https://upwr.edu.pl")
#print(page.content)
soup = BeautifulSoup(page.content, "html.parser")

for a in soup.find_all("a", href=True):
    if a["href"][0] != "/" and a["href"][0] != "#":
        print("Found the URL:", a['href'])
