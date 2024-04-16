import requests

class PriceGetter:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_cryptos_list(self):
        url = "https://api.coingecko.com/api/v3/coins/list?include_platform=false"
        response = requests.get(url)
        return response.json()

    def find_crypto_id_by_symbol(self):
        coins_list = self.get_cryptos_list()
        
        for coin in coins_list:
            if coin != "status" and coin.get('symbol', '').lower() == self.ticker.lower():
                return coin['id']

        return "Cryptocurrency ticker not found."

    def get_crypto_price(self):
        coin_id = self.find_crypto_id_by_symbol()
        
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()

        return data[coin_id]['usd']