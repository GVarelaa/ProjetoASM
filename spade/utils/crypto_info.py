import requests


def get_cryptos_by_ticker(ticker):
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    coins = response.json()

    if response.status_code != 200:
        print(coins)

    matching_coins = []

    for coin in coins:
        if coin.get('symbol', '').lower() == ticker.lower():
            matching_coins.append(coin['id'])

    return matching_coins


def get_coin_id(ticker):
    matching_coins = get_cryptos_by_ticker(ticker)

    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={','.join(matching_coins)}"
    response = requests.get(url)

    if response.status_code == 200:
        coins_data = response.json()
        volumes = {coin['id']: coin['total_volume'] for coin in coins_data}

        return max(volumes, key=volumes.get)
        
    else:
        return "There is no coin with the matching ticker"


def get_market_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/markets"

    params = {
        'vs_currency': 'usd',
        'ids': coin_id,
        'price_change_percentage': '24h'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data[0] if data else "No data available for this cryptocurrency."
    else:
        return "Failed to retrieve data, status code: {}".format(response.status_code)
