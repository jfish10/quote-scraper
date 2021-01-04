from bs4 import BeautifulSoup
import requests



def handle_additional_site(url):
  result = requests.get(url)
  page = result.text

  soup = BeautifulSoup(page, 'html.parser')

  add_quotes = soup.find_all('div', class_='author-quotes')

  new_lst = []
  for quote in add_quotes:
    quotidian = quote.text
    author = quote.find('span', class_='quote-author-name').text
    new_lst.append([quotidian, author])

  return new_lst





