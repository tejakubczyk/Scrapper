from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import requests as req
from functions import go_to_page, write_to_csv, remove_duplicates
import deepl
from classes import Article


soup = go_to_page("https://www.bbc.com/news/technology")
browser = webdriver.Firefox()

#auth_key = "ac80..."
#translator = deepl.Translator(auth_key)

texts = soup.find_all('a')


list_of_links = []

for link in texts:
    if link.get("href") != "" and link.get("href")[0] == "/" and "technology" in link.get("href"):
        # print(link.get('href'))
        new_link = "https://www.bbc.com" + link.get("href")
        list_of_links.append(new_link)


articles = []

for link in list_of_links:
    soup = go_to_page(link)
    title = soup.find("h1", {"id": "main-heading"})
    if title is not None:
        #title = translator.translate_text(title.text, target_lang="PL")
        title = title.text
    contents = soup.find_all(attrs={"class": "ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0", "data-component": "text-block"})
    content = ""
    for article in contents:
        content += article.text
    #if content:
        #content = translator.translate_text(content, target_lang="PL")
    articles.append(Article(title, content).return_list(title, content))

ttl = []
ctn = []
for element in range(len(articles)):
    ttl.append(articles[element][0])
    ctn.append(articles[element][1])

article_as_list = [[ttl[index], ctn[index]] for index in range(len(ttl))]
article_as_list = remove_duplicates(article_as_list)

write_to_csv(article_as_list)
