from spade.behaviour import PeriodicBehaviour
from utils.crypto_info import get_market_data
from spade.message import Message
import jsonpickle

class CollectBehaviour(PeriodicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        msg = Message(to="manager@localhost")
        msg.set_metadata("performative", "INFO")

        data = get_market_data(self.agent.crypto)
        msg.body = jsonpickle.encode(data)

        await self.send(msg)