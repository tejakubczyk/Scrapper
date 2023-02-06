import csv
from bs4 import BeautifulSoup
import requests as req
from classes import Article


def go_to_page(link):
    new_page = req.get(link)
    soup = BeautifulSoup(new_page.text, "html.parser")
    return soup


def write_to_csv(title, content):
    f = open("articles.csv", "w", encoding="utf-8")
    writer = csv.writer(f)
    #header = ['Title', 'Content']
    #writer.writerow(header)
    writer.writerow(title)
    writer.writerow(content)
