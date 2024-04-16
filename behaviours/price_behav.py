from spade.behaviour import PeriodicBehaviour
from utils.crypto_price import PriceGetter
#from spade.message import Message
import random

class PriceBehaviour(PeriodicBehaviour):
    async def run(self):
        print("Price behaviour running...")

        cryptos  = random.sample(self.agent.cryptos,3)

        for crypto in cryptos:
            getter = PriceGetter(crypto)
            price = getter.get_crypto_price()
            print(f"{crypto}: ${price}")