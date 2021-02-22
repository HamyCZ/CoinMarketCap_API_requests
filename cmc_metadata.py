import json
import requests
import config

##metadata
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}
parameters = {
    'slug':'bitcoin,ethereum'
}

req = requests.get(url, headers=headers,params = parameters)
results = json.loads(req.text)

print(json.dumps(results, indent=4))
