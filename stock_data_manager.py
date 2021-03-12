from bs4 import BeautifulSoup
import requests


class StockDataManager:

    def __init__(self):
        pass

    def fetch_data_for_stock(self, ticker):
        stock_ticker = ticker
        yahoo_finance_url = f'https://uk.finance.yahoo.com/quote/{stock_ticker}/key-statistics?p={stock_ticker}'
        peg_ratio = ''
        book_price = ''
        year_change = ''
        sp_year_change = ''

        response = requests.get(yahoo_finance_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        tables = soup.select('table tbody tr td')

        if 'PEG ratio' in tables[8].getText():
            peg_ratio = tables[9].getText()
            print(f'The PEG ratio is {peg_ratio}')
        else:
            print('Issue getting PEG ratio')

        # num = 0
        #
        # for table in tables:
        #     print(num)
        #     print(table.getText())
        #     num += 1

        if 'Price/book' in tables[12].getText():
            book_price = tables[13].getText()
            print(f'The Book price is {book_price}')
        else:
            print('Issue getting Price/book value')

        if '52-week change' in tables[20].getText():
            year_change = tables[21].getText()
            print(f'The year change for {ticker} is {year_change}')
        else:
            print('Issue getting the year change')

        if 'S&P500 52-week change' in tables[22].getText():
            sp_year_change = tables[23].getText()
            print(f'The year change for S&P 500 is {sp_year_change}')
        else:
            print('Issue getting the S&P 500 year change')


        return peg_ratio, book_price, year_change, sp_year_change
