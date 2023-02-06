from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import requests as req
from functions import go_to_page, write_to_csv
import deepl
from classes import Article


soup = go_to_page("https://www.bbc.com/news/technology")
browser = webdriver.Firefox()

texts = soup.find_all('a')
# for text in texts:
#     print(text.get_text())


list_of_links = []

for link in texts:
    if link.get("href") != "" and link.get("href")[0] == "/" and "technology" in link.get("href"):
        # print(link.get('href'))
        new_link = "https://www.bbc.com" + link.get("href")
        list_of_links.append(new_link)

#print(list_of_links)

articles = []

for link in list_of_links:
    soup = go_to_page(link)
    title = soup.find("h1", {"id": "main-heading"})
    if title is not None:
        title = title.text
    contents = soup.find_all(attrs={"class": "ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0", "data-component": "text-block"})
    content = ""
    for article in contents:
        content += article.text
    articles.append(Article(title, content).return_list(title, content))

ttl = []
ctn = []
for element in range(len(articles)):
    ttl.append(articles[element][0])
    ctn.append(articles[element][1])

write_to_csv(ttl, ctn)
