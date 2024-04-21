from spade.agent import Agent
from behaviours.brokerBehav import brokerBehaviour

class brokerAgent(Agent):
    async def setup(self):
        print("Broker agent starting...")

        brokerBehav = brokerBehaviour(period=1)
        self.add_behaviour(brokerBehav)