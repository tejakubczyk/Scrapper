import csv
from bs4 import BeautifulSoup
import requests as req


def go_to_page(link):
    new_page = req.get(link)
    soup = BeautifulSoup(new_page.text, "html.parser")
    return soup


def get_title(soup, list_of_titles):
    title = soup.find("h1", {"id": "main-heading"})
    if title is not None:
        list_of_titles.append(title.text)


def get_content(soup, list_of_contetns):
    articles = soup.find_all("article")
    # blocks_of_text = single_article.find_all("div", {"data-component": "text-block"})
    # content = ""
    #if blocks_of_text != "":
    for each_article in articles:
        print(each_article.text)
        # for block in blocks_of_text:
        #     block = block.text
        #     content += block
        # list_of_contetns.append(content)


def write_to_csv(list_of_elements):
    f = open("articles.csv", "w")
    writer = csv.writer(f)
    writer.writerow(list_of_elements)

