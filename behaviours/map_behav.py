from spade.behaviour import CyclicBehaviour
from spade.message import Message
from utils.crypto_info import get_coinid
import jsonpickle


class MapBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        msg = await self.receive(timeout=10)
        
        if msg:
            print(f"{self.agent.jid} : Message received: {msg.body}")

            data = jsonpickle.decode(msg.body)
            
            if msg.get_metadata("performative") == "MAP":
                coinid, name = get_coinid(data.ticker)

                data.coinid = coinid
                data.name = name

                reply = Message(to=str(msg.sender))
                reply.set_metadata("performative", "MAPREPLY")
                reply.body = jsonpickle.encode(data)

                await self.send(reply)


            