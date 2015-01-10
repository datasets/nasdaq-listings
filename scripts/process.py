''' process.py

    Grab stock listing data from Nasdaq FTP

    - Downloads data from FTP
    - Does some basic cleaning
    - Creates 4 csv files:
        (nasdaq full, nasdaq just symbol/names, all other, nyse only)
    - Creates datapackage.json file w/ schema

    Data Source: ftp://ftp.nasdaqtrader.com/symboldirectory/
    Data Documentation: http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs

    Author: Joe Hand
'''
import pandas as pd
import json

PACKAGE_NAME = 'nasdaq-nyse-listings'
PACKAGE_TITLE = 'Nasdaq and NYSE Listings'

nasdaq_listing = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt'# Nasdaq only
other_listings = 'ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt' # NYSE and other exchanges


def process():
    nasdaq = pd.read_csv(nasdaq_listing,sep='|')
    other =  pd.read_csv(other_listings,sep='|')

    nasdaq = _clean_data(nasdaq)
    other = _clean_data(other)

    # Create a few other data sets
    nasdaq_symbols = nasdaq[['Symbol','Company Name']] # Nasdaq  w/ 2 columns
    nyse = other[other['Exchange'] == 'N'][['ACT Symbol','Company Name']] # NYSE Only

    # (dataframe, filename) datasets we will put in schema & create csv
    datasets = [(nasdaq,'nasdaq-listed'), (nasdaq_symbols,'nasdaq-listed-symbols'),
                (nyse,'nyse-listed'), (other, 'other-listed')]

    for df, filename in datasets:
        df.to_csv('data/' + filename + '.csv', index=False)

    with open("datapackage.json", "w") as outfile:
        json.dump(_create_datapackage(datasets), outfile, indent=4, sort_keys=True)


def _clean_data(df):
    # TODO: do I want to save the file creation time (last row)
    df = df.copy()
    # Remove test listings
    df = df[df['Test Issue'] == 'N']

    # Create New Column w/ Just Company Name
    df['Company Name'] = df['Security Name'].apply(lambda x: x.split('-')[0]) #nasdaq file uses - to separate stock type
    #df['Company Name'] = TODO, remove stock type for otherlisted file (no separator)

    # Move Company Name to 2nd Col
    cols = list(df.columns)
    cols.insert(1, cols.pop(-1))
    df = df.ix[:, cols]

    return df


def _create_file_schema(df, filename):
    fields = []
    for name, dtype in zip(df.columns,df.dtypes):
        if str(dtype) == 'object' or str(dtype) == 'boolean': # does datapackage.json use boolean type?
            dtype = 'string'
        else:
            dtype = 'number'

        fields.append({'name':name, 'description':'', 'type':dtype})

    return {
            'name': filename,
            'path': 'data/' + filename + '.csv',
            'format':'csv',
            'mediatype': 'text/csv',
            'schema':{'fields':fields}
            }


def _create_datapackage(datasets):
    resources = []
    for df, filename in datasets:
        resources.append(_create_file_schema(df,filename))

    return {
            'name': PACKAGE_NAME,
            'title': PACKAGE_TITLE,
            'license': '',
            'resources': resources,
            }



if __name__ == '__main__':
    process()
