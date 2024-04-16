from spade.behaviour import CyclicBehaviour
from utils.crypto_info import CryptoInfo
#from spade.message import Message
import random

class MapBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        msg = await self.receive(timeout=10)

        if msg:
            print(f"{self.agent.jid} : Message received: {msg.body}")
            info = CryptoInfo(self.agent.ticker)
            print(info.coin_id)
            
        else:
            print(f"{self.agent.jid} did not received any message after 10 seconds")