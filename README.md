# CoinMarketCap - Python and Cryptocurrencies
This project was entierly made thanks to an Udemy course created by Ian Annase 'Python & Cryptocurrency: Build 5 Real World Applications' https://www.udemy.com/share/101wh6A0QYcV1bQHg=/ and personal aim is to get familiar with Python and API(s).



### A Cryptocurrency Portfolio App
To track all the crypto assets. You can total value of all your crypto assets combined along with detailed information about each one.
Files required to run:
```
cmc_portfolio.py
config.py
portfolio.txt
```

### A Real-Time Price Alert App
Get notification when cryptocurrencies hit certain prices.
Files required to run:
```
cmc_alerts.py
config.py
alerts.txt
```

### Cryptocurreny Ranking App
Sort by rank, daily percentage change, or by newest cryptocurrencies.
Files required to run:
```
cmc_top100.py
config.py
```

### Store Real-Time Information of Cryptocurrencies in Excel
Learn to store cryptocurrency information inside of excel workbooks using Python.
Files required to run:
```

config.py
```

### CoinMarketCap API details
Shows how many daily/monthly credits use has left when using free CMC API key
Files required to run:
```
cmc_APIkey_statistics.py
config.py
```



## Required configuration steps
* register at https://pro.coinmarketcap.com/account for your free API key
* in same folder as the python files create ```config.py``` file with folowing structure where you list your API key and calculation currency you want to use in your results

```
API_KEY='<your_API_key_from_CMC_here>'
CCY='GBP'
```
