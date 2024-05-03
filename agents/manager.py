from spade.agent import Agent
from behaviours.manager_behav import ManagerBehaviour
from behaviours.check_behav import CheckBehaviour

class ManagerAgent(Agent):
    # Tuplo -> Preço, Quantiadade de Tokens
    stoploss = 20 # percentagem stoploss -> definir pela interface
    takeprofit = 40 # percentagem takeprofit -> definir pela interface
    balance = None
    portfolio = {
            "Bitcoin": (10.0, 5.0),
            "Ethereum": (5, 3.0),
            "Litecoin": (10, 2.0),
            "Ripple": (10, 1.5),
            "Bitcoin Cash": (15, 6.0),
            "Cardano": (8, 1.2),
            "Polkadot": (12, 4.5),
            "Stellar": (20, 0.8),
            "Chainlink": (6, 5.2),
            "USD Coin": (100, 1.0),
            "Binance Coin": (3, 20.0),
            "Tether": (200, 1.0),
            "Dogecoin": (50, 0.3),
            "Wrapped Bitcoin": (7, 40000.0),
            "Uniswap": (25, 30.0),
            "Bitcoin SV": (4, 180.0),
            "Aave": (2, 400.0),
            "EOS": (30, 3.5),
            "Monero": (3, 150.0),
            "TRON": (500, 0.05),
            "NEO": (12, 20.0)
        }
    influencers = ["Influencer 1", "Influencer 2", "Influencer 3"] 
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
    threshold = 0
    loss = 0
    
    
    async def setup(self):
        print(f"{str(self.jid).partition('@')[0]} : starting...")

        self.a = ManagerBehaviour()
        self.b = CheckBehaviour(period=10) # 10 segundos

        self.add_behaviour(self.a)
        self.add_behaviour(self.b)
    
    def get_portfolio(self):
        return self.portfolio
    
    def get_influencers(self):
        return self.influencers
    
    def add_influencer(self, influencer):
        self.influencers.append(influencer)
    
    def remove_influencer(self, influencer):
        self.influencers.remove(influencer)
    
    def get_history(self):
        return self.history
    
    def add_history(self, data):
        self.history.append(data)
    
    def get_threshold(self):
        return self.threshold
    
    def set_threshold(self, threshold):
        self.threshold = threshold
    
    def get_loss(self):
        return self.loss
    
    def set_loss(self, loss):
        self.loss = loss
    