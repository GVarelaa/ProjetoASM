from spade.agent import Agent
from behaviours.manager_behav import ManagerBehaviour

class ManagerAgent(Agent):
    portfolio = {}
    
    async def setup(self):
        print(f"{str(self.jid).partition('@')[0]} : starting...")

        self.b = ManagerBehaviour()
        self.add_behaviour(self.b)