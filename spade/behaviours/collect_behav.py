from spade.behaviour import PeriodicBehaviour
from utils.crypto_info import CryptoInfo
#from spade.message import Message
import random

class CollectBehaviour(PeriodicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        tickers  = random.sample(self.agent.cryptos, 3)

        for ticker in tickers:
            info = CryptoInfo(ticker)
            market_data = info.get_market_data()