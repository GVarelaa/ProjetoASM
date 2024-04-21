from spade.agent import Agent
from behaviours.broker_behav import BrokerBehaviour

class brokerAgent(Agent):
    async def setup(self):
        print("Broker agent starting...")

        brokerBehav = BrokerBehaviour(period=1)
        self.add_behaviour(brokerBehav)