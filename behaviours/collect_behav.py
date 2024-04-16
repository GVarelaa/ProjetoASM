from spade.behaviour import PeriodicBehaviour
from utils.crypto_info import CryptoInfo
#from spade.message import Message
import random

class CollectBehaviour(PeriodicBehaviour):
    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        tickers  = random.sample(self.agent.cryptos,3)

        for ticker in tickers:
            print(ticker)
            info = CryptoInfo(ticker)
            print(info.coin_id)
            market_data = info.get_market_data()
            print(str(market_data) + "\n")