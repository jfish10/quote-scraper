from bs4 import BeautifulSoup
import requests
import csv
import additional_quotes


result = requests.get('http://quotes.toscrape.com/')
page = result.text

soup = BeautifulSoup(page, 'html.parser')

quotes = soup.find_all('div', class_='quote')

scraped = []
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    scraped.append([text, author])


additional_quotes = additional_quotes.handle_additional_site('https://www.keepinspiring.me/famous-quotes/')



with open('famous-quotes.csv', 'w') as quotations:
   writer = csv.writer(quotations, delimiter=',')
   for quote in scraped:
     writer.writerow(quote)
   for quote in additional_quotes:
     writer.writerow(quote)



print("Quotes added successfully!")



