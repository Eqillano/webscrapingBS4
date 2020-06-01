import requests

from pages.quotes_page import QuotesPage


page = requests.get('http://quotes.toscrape.com')
page.encoding = 'utf-8'
page_content = page.content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote.content)
