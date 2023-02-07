import csv
from bs4 import BeautifulSoup
import requests as req
from classes import Article


def go_to_page(link):
    new_page = req.get(link)
    soup = BeautifulSoup(new_page.text, "html.parser")
    return soup


def write_to_csv(art_list):
    f = open("articles.csv", "w", encoding="utf-8")
    writer = csv.writer(f)
    header = ['Title', 'Content']
    writer.writerow(header)
    for index in range(len(art_list)):
        if art_list[index][0] and art_list[index][1]:
            writer.writerow([art_list[index][0], art_list[index][1]])


def remove_duplicates(some_list):
    unique_list = []
    for element in some_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
