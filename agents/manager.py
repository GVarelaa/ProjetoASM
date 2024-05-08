from spade.agent import Agent
from behaviours.manager_behav import ManagerBehaviour
from behaviours.check_behav import CheckBehaviour

class ManagerAgent(Agent):
    stoploss = 10 # percentagem stoploss -> definir pela interface
    takeprofit = 5 # percentagem takeprofit -> definir pela interface
    trade_balance = 0
    balance = None
    portfolio = {}

    history = ["JohnDoe : selling 7 of Ethereum at 13974.87",
    "JohnDoe : buying 3 of Litecoin at 23150.47",
    "JohnDoe : buying 2 of Bitcoin at 35298.93",
    "JohnDoe : buying 1 of Litecoin at 28477.35",
    "JohnDoe : buying 10 of Ethereum at 36615.44",
    "JohnDoe : buying 4 of Bitcoin at 30194.38",
    "JohnDoe : buying 3 of Ripple at 14872.55",
    "JohnDoe : selling 10 of Litecoin at 17177.79",
    "JohnDoe : buying 5 of Ripple at 28326.31",
    "JohnDoe : selling 3 of Ripple at 26331.95",
    "JohnDoe : selling 7 of Ethereum at 13974.87",
    "JohnDoe : buying 3 of Litecoin at 23150.47",
    "JohnDoe : buying 2 of Bitcoin at 35298.93",
    "JohnDoe : buying 1 of Litecoin at 28477.35",
    "JohnDoe : buying 10 of Ethereum at 36615.44",
    "JohnDoe : buying 4 of Bitcoin at 30194.38",
    "JohnDoe : buying 3 of Ripple at 14872.55",
    "JohnDoe : selling 10 of Litecoin at 17177.79",
    "JohnDoe : buying 5 of Ripple at 28326.31",
    "JohnDoe : selling 3 of Ripple at 26331.95",
    "JohnDoe : buying 8 of Ethereum at 22937.68",
    "JohnDoe : selling 6 of Bitcoin at 41544.73",
    "JohnDoe : selling 2 of Litecoin at 42613.39",
    "JohnDoe : buying 7 of Bitcoin at 17697.01",
    "JohnDoe : buying 9 of Ethereum at 43480.67",
    "JohnDoe : selling 5 of Ethereum at 29412.56",
    "JohnDoe : buying 10 of Bitcoin at 42602.23",
    "JohnDoe : selling 4 of Ripple at 20268.89",
    "JohnDoe : buying 6 of Litecoin at 41815.12",
    "JohnDoe : selling 1 of Bitcoin at 38518.26",
    "JohnDoe : selling 9 of Litecoin at 20814.61",
    "JohnDoe : selling 8 of Ripple at 22707.09",
    "JohnDoe : buying 2 of Ethereum at 24352.03",
    "JohnDoe : selling 5 of Litecoin at 19364.14",
    "JohnDoe : buying 4 of Ripple at 14123.99",
    "JohnDoe : selling 7 of Bitcoin at 43621.89",
    "JohnDoe : buying 1 of Ethereum at 47983.38",
    "JohnDoe : buying 6 of Ripple at 33601.81",
    "JohnDoe : buying 3 of Litecoin at 37792.76",
    "JohnDoe : selling 10 of Ethereum at 48928.17"]
    
    
    async def setup(self):
        print(f"{str(self.jid).partition('@')[0]} : starting...")

        self.a = ManagerBehaviour()
        self.b = CheckBehaviour(period=30) # 10 segundos

        self.add_behaviour(self.a)
        self.add_behaviour(self.b)
    
    def get_history(self):
        return self.history
    
    def add_history(self, data):
        self.history.append(data)
    