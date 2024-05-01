from datetime import datetime
import jsonpickle
from spade.behaviour import CyclicBehaviour
from spade.message import Message

from utils.brokerMessage import brokerMessage

class ManagerBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")
        # print portfolio
        
        # enviar decisão ao broker - exemplo
        #request = brokerMessage("buy", "BTC", 10, 100)
        #msg = Message(to="broker@localhost")
        #msg.set_metadata("performative", "request")
        #msg.body = jsonpickle.encode(request)
        #await self.send(msg)
        
        msg = await self.receive(timeout=10)

        if msg:
            # receber trends do twitter
            #if msg.get_metadata("performative") == "trends":
            #    trends = jsonpickle.decode(msg.body)
            #    print("MANAGER")
            #    print(trends)
            
            # adiciona resposta do broker ao histórico
            #if msg.get_metadata("performative") == "confirm":
            #    message = jsonpickle.decode(msg.body)
            #    self.agent.add_history(message.getMessage())
            
            data = jsonpickle.decode(msg.body)
            
            print(f"{str(self.agent.jid).partition('@')[0]} : message received with content: " + str(data))

            if msg.get_metadata("performative") == "CALL":
                msg = Message(to="mapper@localhost")
                msg.set_metadata("performative", "MAP")
                msg.body = jsonpickle.encode(data)

                await self.send(msg)
                
            elif msg.get_metadata("performative") == "MAPREPLY":
                # Se não estiver no portfólio então compra
                coin_id = data["coin_id"]

                if coin_id not in self.agent.portfolio:
                    self.agent.portfolio["coin_id"] = (0, 0)

                    # Dar trigger a um agente collector e enviar mensagem ao broker pra comprar

        else:
            print(f"{str(self.agent.jid).partition('@')[0]} : message timeout after 10 seconds")