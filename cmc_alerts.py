##
## "Infinte" loop to check if price of crypto(s) is higher than defined in alerts.txt  placed in same folder as this .py
##
import json
import requests
import time
import config

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.API_KEY,
}

print("Alerts tracking")
already_hit_symbols = []
a = 0

while a < 3:
    with open('alerts.txt') as inp:
        for line in inp:
            ticker, amount = line.split()
            ticker = ticker.upper()

            parameters = {
                'symbol': ticker,
                'convert': config.CCY
            }
            request = requests.get(url, headers=headers, params=parameters)
            results = json.loads(request.text)

            currency = results['data'][ticker]
            name = currency['name']
            symbol = currency['symbol']
            price = currency['quote'][config.CCY]['price']

            print(name + ' is ' + str(format(round(price, 2))) + '  >=   ' + str(amount))

            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                print('We have hit ' + symbol + ' for price of ' + str(amount))

                already_hit_symbols.append(symbol)

        print("...")
        print(already_hit_symbols)
        time.sleep(60)

a += 1
