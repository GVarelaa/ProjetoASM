import jsonpickle
from spade.behaviour import CyclicBehaviour
from spade.message import Message

from utils.trade import Trade
from utils.crypto_info import get_market_data

class BrokerBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        msg = await self.receive(timeout=10)

        if msg:
            data = jsonpickle.decode(msg.body)
            
            performative = msg.get_metadata("performative")

            print(f"{str(self.agent.jid).partition('@')[0]} : {performative}")
            print(f"{str(self.agent.jid).partition('@')[0]} : message received with content: " + str(data))

            if msg.get_metadata("performative") == "BUY":
                # NA REALIDADE TERÍAMOS DE USAR A API DE UMA CEX/DEX E COMPRAR -> VAMOS USAR UMA SIMULAÇÃO
                coin_data = get_market_data(data.coinid)

                price = coin_data["quote"]["USD"]["price"]
                quantity = data.balance / price
                    
                data.price = price
                data.quantity = quantity
                data.balance = price * quantity

                msg = Message(to=str(msg.sender)) 
                msg.set_metadata("performative", "BUYREPLY") 
                msg.body = jsonpickle.encode(data)
                
                await self.send(msg)
            
            elif msg.get_metadata("performative") == "SELL":
                # NOVAMENTE UMA SIMULAÇÃO
                coin_data = get_market_data(data.coinid)

                price = coin_data["quote"]["USD"]["price"]
                balance = data.quantity * price

                data.price = price
                data.balance = balance

                msg = Message(to=str(msg.sender)) 
                msg.set_metadata("performative", "SELLREPLY") 
                msg.body = jsonpickle.encode(data)
                
                await self.send(msg)

            #else:
                    #msg_to_manager.set_metadata("performative", "refuse") 