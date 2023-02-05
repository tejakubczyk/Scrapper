from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import requests as req
from functions import get_content, get_title, go_to_page, write_to_csv


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

print(list_of_links)


titles = []
content = []

for link in list_of_links:
    new_page_soup = go_to_page(link)
    get_title(new_page_soup, titles)
    get_content(new_page_soup, content)

titles = list(dict.fromkeys(titles))
#print(titles)
content = list(dict.fromkeys(content))
#print(content)

print(content)

# article = [[titles[index], content[index]] for index in range(0, len(titles))]
# write_to_csv(article)
