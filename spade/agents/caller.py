from spade.agent import Agent
from behaviours.caller_behav import CallerBehaviour

class CallerAgent(Agent):
    user = "MacnBTC" #"randommeme65920"
    last_tweet = {}

    async def setup(self):
        print(f"{str(self.jid).partition('@')[0]} : starting...")

        self.b = CallerBehaviour(period=10)
        self.add_behaviour(self.b)