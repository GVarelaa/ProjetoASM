from spade.behaviour import CyclicBehaviour
from spade.message import Message
from utils.crypto_info import get_coin_id
import jsonpickle


class MapBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        msg = await self.receive(timeout=10)
        
        if msg:
            print(f"{self.agent.jid} : Message received: {msg.body}")

            data = jsonpickle.decode(msg.body)
            
            if msg.get_metadata("performative") == "MAP":
                coin_id = get_coin_id(data["ticker"])
                
                reply = Message(to=msg.sender)
                reply.set_metadata("performative", "MAPREPLY")
                reply.body = jsonpickle({"coin_id": coin_id}) # Meter o nome também para dar display na interface

                await self.send(reply)
            
        else:
            print(f"{self.agent.jid} did not received any message after 10 seconds")


            