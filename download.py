import csv
import requests
from bs4 import BeautifulSoup
import threading

proxies = {
    'http': 'http://dcRezG:kjrDLs@193.7.199.142:8000',
    'https': 'http://dcRezG:kjrDLs@193.7.199.142:8000',
}


url = "https://www.rockpapershotgun.com/pubg-guns-weapons-update-6-2-pubg-gun-stats-best-weapons-in-season-6"


def scrape_data(url):

    response = requests.get(url, timeout=10, proxies=proxies)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find_all('table')[1]

    rows = table.select('tbody > tr')

    header = [th.text.rstrip() for th in rows[0].find_all('th')]

    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)

scrape_data(url)
