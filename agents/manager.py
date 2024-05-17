from spade.agent import Agent
from behaviours.manager_behav import ManagerBehaviour
from behaviours.check_behav import CheckBehaviour

class ManagerAgent(Agent):
    stoploss = 10 # percentagem stoploss -> definir pela interface
    takeprofit = 5 # percentagem takeprofit -> definir pela interface
    trade_balance = 0
    balance = 10000 # default value
    portfolio = {}
    history = []
    
    async def setup(self):
        print(f"{str(self.jid).partition('@')[0]} : starting...")

        self.a = ManagerBehaviour()
        self.b = CheckBehaviour(period=30) # 30 segundos

        self.add_behaviour(self.a)
        self.add_behaviour(self.b)
    
    