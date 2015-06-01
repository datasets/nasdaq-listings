List of companies in the NASDAQ exchanges.

## Data

Data and documentation are available on [NASDAQ's official webpage](http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs). Data is updated regularly on the FTP site.

The file used in this repository:
* [NASDAQ Listed Securities](ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt)

Notes:

* Company Name is a parsed field using the Security Name field.
* Test Listings are excluded in the final dataset

## Preparation

You need python plus pandas library tool installed to run the
scripts. You also probably need to be on Linux/Unix or Mac for the shell
scripts to work.


#### all datasets

***Creates all csv files and datapackage.json***

Run python script:

      python scripts/process.py


## License

This Data Package is licensed by its maintainers under the [Public Domain Dedication and License (PDDL)](http://opendatacommons.org/licenses/pddl/1.0/).

Refer to the [Copyright notice](http://www.nasdaqtrader.com/Trader.aspx?id=CopyDisclaimMain) of the source dataset for any specific restrictions on using these data in a public or commercial product. Copyright © 2010, The NASDAQ OMX Group, Inc. All rights reserved.
