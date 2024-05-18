from spade.agent import Agent
from behaviours.broker_behav import BrokerBehaviour

class BrokerAgent(Agent):
    async def setup(self):
        brokerBehav = BrokerBehaviour()
        
        self.add_behaviour(brokerBehav)