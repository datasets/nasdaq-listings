<a className="gh-badge" href="https://datahub.io/core/nasdaq-listings"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

List of companies in the NASDAQ exchanges.

## Data

Data and documentation are available on [NASDAQ's official webpage](http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs). Data is updated regularly on the FTP site.

The file used in this repository:
* [NASDAQ Listed Securities](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt)

Notes:

* Company Name is a parsed field using the Security Name field (text before the first ' - ').
* Test listings (Test Issue = Y) are **included** in the dataset and can be identified by the `Test Issue` field.
* A "File Creation Time" footer row from the NASDAQ source file appears at the end of both CSVs and should be ignored when processing the data.

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
