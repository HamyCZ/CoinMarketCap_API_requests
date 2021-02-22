import json
import requests
import config
from colorama import Fore, Style

url = 'https://pro-api.coinmarketcap.com/v1/key/info'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.API_KEY,
}

request = requests.get(url, headers=headers)
results = json.loads(request.text)

data = results['data']

current_day_cr_max = '{:,}'.format(data['plan']['credit_limit_daily'])
current_day_cr_left = '{:,}'.format(data['usage']['current_day']['credits_used'])

current_month_cr_max = '{:,}'.format(data['plan']['credit_limit_monthly'])
current_month_cr_left = '{:,}'.format(data['usage']['current_month']['credits_used'])

daily_reset = data['plan']['credit_limit_daily_reset']

print('Daily usage is ' + Fore.CYAN + current_day_cr_left + Style.RESET_ALL + ' out of ' + current_day_cr_max)
print('Monthly usage is ' + Fore.CYAN + current_month_cr_left + Style.RESET_ALL + ' out of ' + current_month_cr_max)
print(f'Daily reset in: {daily_reset}')
