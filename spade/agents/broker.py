from spade.agent import Agent
from behaviours.broker_behav import BrokerBehaviour

class BrokerAgent(Agent):
    async def setup(self):
        print("Broker agent starting...")

        brokerBehav = BrokerBehaviour()
        self.add_behaviour(brokerBehav)