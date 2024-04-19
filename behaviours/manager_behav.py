import pickle
from datetime import datetime
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class ManagerBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        msg = await self.receive(timeout=10)

        if msg:
            #decoded_data = pickle.loads(msg.body)

            if msg.get_metadata("performative") == "CALL":
                print(f"{str(self.agent.jid).partition('@')[0]} : message received with content: " + str(msg.body))

                # Se não estiver no portfólio então compra

        else:
            print(f"{str(self.agent.jid).partition('@')[0]} : message timeout after 10 seconds")