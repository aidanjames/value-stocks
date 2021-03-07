import pandas as pd
from bs4 import BeautifulSoup
import requests


WIKI_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
YAHOO_FINANCE_URL = 'https://uk.finance.yahoo.com/quote/FISV/key-statistics?p='

# Returns a list of tables on from url provided
# The first table is the one we need
# I've reduced the columns to the ones we care about.
df = pd.read_html(WIKI_URL)[0][['Symbol', 'Security', 'GICS Sector']]
print(df.head(3))
# Change the column names to 'Ticker', 'Company', and 'Category'
df.rename(columns={'Symbol': 'Ticker', 'Security': 'Company', 'GICS Sector': 'Category'}, inplace=True)

# Write to a CSV
df.to_csv('tickers', index=False)

response = requests.get(YAHOO_FINANCE_URL + 'FISV').text
soup = BeautifulSoup(response, 'html.parser')
print(soup)