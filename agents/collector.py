from spade.agent import Agent
from behaviours.collect_behav import CollectBehaviour

class CollectorAgent(Agent):
    crypto = None

    async def setup(self):
        print(f"{str(self.jid).partition('@')[0]} : starting...")

        self.b = CollectBehaviour(period=60) # 60 segundos
        self.add_behaviour(self.b)