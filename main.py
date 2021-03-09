import pandas as pd
from bs4 import BeautifulSoup
import requests
from stock_data_manager import StockDataManager

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

stock_data_manager = StockDataManager()
stock_data_manager.fetch_data_for_stock('FISV')