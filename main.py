from bs4 import BeautifulSoup
import requests
import csv


result = requests.get('http://quotes.toscrape.com/')
page = result.text

soup = BeautifulSoup(page, 'html.parser')

quotes = soup.find_all('div', class_='quote')

scraped = []
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    scraped.append([text, author])

for scrape in scraped:
  print(scrape)

with open('famous-quotes.csv', 'a') as quotations:
   writer = csv.writer(quotations, delimiter=',')
   for quote in scraped:
     writer.writerow(quote)