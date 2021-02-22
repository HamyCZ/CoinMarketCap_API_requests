import json
import requests
import config
import xlsxwriter

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}

start = 1
f = 1
calculation_currency = config.CCY

crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()
crypto_sheet.write('A1', "Name")
crypto_sheet.write('B1', "Symbol")
crypto_sheet.write('C1', "MarketCap")
crypto_sheet.write('D1', "Price")
crypto_sheet.write('E1', "24h Volume")
crypto_sheet.write('F1', "Hour change")
crypto_sheet.write('G1', "Day Change")
crypto_sheet.write('H1', "Week Change")


for i in range(10):
    parameters = {
        'convert': calculation_currency,
        'start': str(start),
        'limit': '100'
        # 'limit': default is 100 (max is 5000) that's why we get with this range 1000 results
    }
    request = requests.get(url, headers=headers, params=parameters)
    results = json.loads(request.text)

    data = results['data']
    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quote'][calculation_currency]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        crypto_sheet.write(f, 0, name)
        crypto_sheet.write(f, 1, symbol)
        crypto_sheet.write(f, 2, str(market_cap))
        crypto_sheet.write(f, 3, str(price))
        crypto_sheet.write(f, 4, str(volume))
        crypto_sheet.write(f, 5, str(hour_change))
        crypto_sheet.write(f, 6, str(day_change))
        crypto_sheet.write(f, 7, str(week_change))

        f += 1
start += 1

crypto_workbook.close()
print('Files are now created in the folder')

