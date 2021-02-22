import json
import requests
import config
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from datetime import datetime

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
url_total_mc = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.API_KEY,
}

calculation_currency = config.CCY

parameters_total_mc = {
    'convert': calculation_currency
}

request_total_mc = requests.get(url_total_mc, headers=headers, params=parameters_total_mc)
results_total_mc = json.loads(request_total_mc.text)

data_total_mc = results_total_mc['data']['quote'][calculation_currency]
total_mc = '{:,}'.format(data_total_mc['total_market_cap'])
total_mc_volume = '{:,}'.format(data_total_mc['total_volume_24h'])
total_altcoin_mc = '{:,}'.format(data_total_mc['altcoin_market_cap'])
total_altcoin_volume = '{:,}'.format(data_total_mc['altcoin_volume_24h'])

while True:
    print(
        f'Global market cap: {total_mc} {calculation_currency} and total 24h volume: {total_mc_volume} {calculation_currency}')
    print('1 - Top cryptocurrencies sorted by market cap')
    print('2 - Cryptocurrencies sorted by 24 hour change')
    print('3 - Newest cryptocurencies')
    print('0 - Exit')
    print()
    choice = input('Pick your option: ')

    user_input = ''
    sorting_info = 'desc'

    if choice == '1':
        user_input = 'market_cap'
        limit = '7'
    elif choice == '2':
        user_input = 'percent_change_24h'
        limit = '20'
    elif choice == '3':
        user_input = 'date_added'
        limit = '25'
        sorting_info = 'asc'
    else:
        print('Ending script')
        break

    parameters = {
        'convert': calculation_currency,
        'sort': user_input,
        'limit': limit,
        'sort_dir': sorting_info
    }
    request = requests.get(url, headers=headers, params=parameters)
    results = json.loads(request.text)

    # print(json.dumps(results,indent=4))

    data = results['data']

    table = PrettyTable(
        ['Name', 'Symbol', 'Total/Max supply', 'Date added', calculation_currency + ' price', '1h', '24h', '7d', '30d',
         'Platform', 'Market cap'])

    for currency in data:
        name = currency['name']
        symbol = currency['symbol']
        max_supply = currency['max_supply']
        current_supply = '{:,.2f}'.format(currency['circulating_supply'])

        if currency['platform'] is None:
            platform = 'n/a'
        else:
            platform = currency['platform']['name']

        date_added = currency['date_added']
        price = currency['quote'][calculation_currency]['price']
        price_format = '{:,.4f}'.format(price)
        volume1h = currency['quote'][calculation_currency]['percent_change_1h']
        volume1h_format = '{:,.2f}'.format(volume1h)
        change1d = currency['quote'][calculation_currency]['percent_change_24h']
        change1d_format = '{:,.2f}'.format(change1d)
        change7d = currency['quote'][calculation_currency]['percent_change_7d']
        change7d_format = '{:,.2f}'.format(change7d)
        change30d = currency['quote'][calculation_currency]['percent_change_30d']

        # Value handling and formatting
        if change30d is not None:
            change30d_format = '{:,.2f}'.format(change30d)
        else:
            change30d_format = change30d

        market_cap = '{:,.2f}'.format(currency['quote'][calculation_currency]['market_cap'])

        if volume1h is not None:
            if float(volume1h) > 0:
                volume1h_format = Back.GREEN + str(volume1h_format) + '%' + Style.RESET_ALL
            else:
                volume1h_format = Back.RED + str(volume1h_format) + '%' + Style.RESET_ALL

        if change1d is not None:
            if float(change1d) > 0:
                change1d_format = Back.GREEN + str(change1d_format) + '%' + Style.RESET_ALL
            else:
                change1d_format = Back.RED + str(change1d_format) + '%' + Style.RESET_ALL

        if change7d is not None:
            if float(change7d) > 0:
                change7d_format = Back.GREEN + str(change7d_format) + '%' + Style.RESET_ALL
            else:
                change7d_format = Back.RED + str(change7d_format) + '%' + Style.RESET_ALL

        if change30d is not None:
            if float(change30d) > 0:
                change30d_format = Back.GREEN + str(change30d_format) + '%' + Style.RESET_ALL
            else:
                change30d_format = Back.RED + str(change30d_format) + '%' + Style.RESET_ALL

        if market_cap is None:
            market_cap = Fore.CYAN + '{:,}'.format(market_cap) + Style.RESET_ALL

        date_added_conv = datetime.strptime(date_added, '%Y-%m-%dT%H:%M:%S.%f%z')
        date_added_short = datetime.strftime(date_added_conv, "%d-%m-%Y")

        if max_supply is None:
            max_supply = 'undefined'
        else:
            max_supply = '{:,}'.format(max_supply)

        table.add_row([name,
                       symbol,
                       # str(tags),
                       str(current_supply) + '/' + str(max_supply),
                       str(date_added_short),
                       str(price_format),
                       str(volume1h_format),
                       str(change1d_format),
                       str(change7d_format),
                       change30d_format,
                       platform,
                       calculation_currency + ' ' + str(market_cap)])

    print(table)

    choice = input('Run again? (y/n) ')
    if choice != 'y':
        break
