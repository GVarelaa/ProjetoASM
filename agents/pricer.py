from spade.agent import Agent
from behaviours.price_behav import PriceBehaviour

class PricerAgent(Agent):
    cryptos = ["BTC", "ETH", "ONDO"]

    async def setup(self):
        print(f"{str(self.jid).partition('@')[0]} : starting...")
        self.b = PriceBehaviour(period=4)
        self.add_behaviour(self.b)