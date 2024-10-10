import requests
import pandas as pd

NASDAQ_URL = 'https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt'

def transform_nasdaq_listed_symbol():
    resp = requests.get(NASDAQ_URL)

    data = resp.text.split('\n')
    data = [row.split('|') for row in data]
    df = pd.DataFrame(data[1:], columns=data[0])

    # Transform data
    df.columns = df.columns.str.replace('\r', '', regex=False)
    df = df.map(lambda x: x.replace('\r', '') if isinstance(x, str) else x)

    # Create nasdaq_listed.csv and nasdaq_listed_symbol.csv
    nasdaq_listed = df[['Symbol', 'Security Name']]
    nasdaq_listed.to_csv('data/nasdaq-listed.csv', index=False)
    nasdaq_listed_symbol = df
    nasdaq_listed_symbol['Company Name'] = nasdaq_listed_symbol['Security Name'].str.split(' - ').str[0]
    last_col = nasdaq_listed_symbol.pop(nasdaq_listed_symbol.columns[-1])
    nasdaq_listed_symbol.insert(1, last_col.name, last_col)
    nasdaq_listed_symbol.to_csv('data/nasdaq-listed-symbols.csv', index=False)
    print('nasdaq-listed.csv and nasdaq-listed-symbols.csv saved.')

if __name__ == '__main__':
    transform_nasdaq_listed_symbol()