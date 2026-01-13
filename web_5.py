import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    tag = soup.find('td', {"id": "mp-right"})
    h = tag.find_all("h2")
    content = [span.text for span in h]

    with open("wiki.csv", "w") as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(content)

Extract(url = "https://en.wikipedia.org/wiki/Main_Page")