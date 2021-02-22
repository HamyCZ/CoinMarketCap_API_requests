import json
import requests
import config
from prettytable import PrettyTable
from colorama import Back, Style


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}

calculation_currency = config.CCY
portfolio_value = 0.00
last_updated = 0
ptf_percentage_data = []
asset_data = []
z = 0

table = PrettyTable(['Asset', 'My Coins', 'Price', calculation_currency + ' value', '1h', '24h', '7d', '30d'])
table.title = 'My Portfolio'
table2 = PrettyTable(['Ticker','Percentage'])
table2.title = 'Coin percentage split'
table2.header = False

with open("portfolio.txt") as inp:
    for line in inp:
        ticker, amount = line.split()
        ticker = ticker.upper()

        parameters_2 = {
            'symbol': ticker,
            'convert': calculation_currency
        }
        request = requests.get(url, headers=headers, params=parameters_2)
        results = json.loads(request.text)

        currency = results['data'][ticker]
        name = currency['name']
        last_updated = currency['last_updated']
        symbol = currency['symbol']
        quotes = currency['quote'][calculation_currency]
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        month_change = quotes['percent_change_30d']
        price = quotes['price']

        value = float(price) * float(amount)
        portfolio_value += value
        value_string = '{:,}'.format(round(value, 2))
        formatted_price = '{:,}'.format(round(price, 2))


        ptf_percentage_data.append(value)
        asset_data.append(name)

        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change > 0:
            week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        if month_change > 0:
            month_change = Back.GREEN + str(month_change) + '%' + Style.RESET_ALL
        else:
            month_change = Back.RED + str(month_change) + '%' + Style.RESET_ALL

        table.add_row([name + '(' + symbol + ')',
                       str(amount),
                       str(formatted_price),
                       value_string,
                       str(hour_change),
                       str(day_change),
                       str(week_change),
                       str(month_change)])
        table.align = 'l'

    for val in ptf_percentage_data:
        x = val / portfolio_value * 100
        x = '{:,.2f}'.format(round(x, 2))
        y = asset_data[z]
        table2.add_row([str(y), str(x) + '%'])
        z += 1

print(table2, '\n \n', table)


portfolio_value_string = '{:,}'.format(round(portfolio_value, 2))
print("Last entry timestamp update: " + last_updated)
print("Total portfolio value in " + calculation_currency + " : " + Back.GREEN + portfolio_value_string + Style.RESET_ALL)





