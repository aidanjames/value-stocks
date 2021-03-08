import pandas as pd
from bs4 import BeautifulSoup
import requests

WIKI_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

stock_ticker = 'PTON'
YAHOO_FINANCE_URL = f'https://uk.finance.yahoo.com/quote/{stock_ticker}/key-statistics?p={stock_ticker}'

# Returns a list of tables on from url provided
# The first table is the one we need
# I've reduced the columns to the ones we care about.
# df = pd.read_html(WIKI_URL)[0][['Symbol', 'Security', 'GICS Sector']]
# print(df.head(3))
# Change the column names to 'Ticker', 'Company', and 'Category'
# df.rename(columns={'Symbol': 'Ticker', 'Security': 'Company', 'GICS Sector': 'Category'}, inplace=True)

# Write to a CSV
# df.to_csv('tickers', index=False)

response = requests.get(YAHOO_FINANCE_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# TODO Get the PEG ratio for a single stock
tables = soup.select('table tbody tr td')

peg_ratio = tables[9].getText()

num = 0

for table in tables:
    print(num)
    print(table.getText())
    num += 1

# TODO Get the book price for a single stock

book_price = tables[13].getText()
print(book_price)
print(peg_ratio)