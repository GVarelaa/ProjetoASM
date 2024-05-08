import jsonpickle
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from agents.collector import CollectorAgent

from utils.brokerMessage import brokerMessage
from utils.asset import Asset
from utils.trade import Trade


XMPP_SERVER = 'localhost'
PASSWORD = 'admin'

class ManagerBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):        
        msg = await self.receive(timeout=10)

        if msg:
            data = jsonpickle.decode(msg.body)
            
            performative = msg.get_metadata("performative")

            print(f"{str(self.agent.jid).partition('@')[0]} : {performative}")
            print(f"{str(self.agent.jid).partition('@')[0]} : message received with content: " + str(data))

            if msg.get_metadata("performative") == "CALL":
                msg = Message(to="mapper@localhost")
                msg.set_metadata("performative", "MAP")
                msg.body = jsonpickle.encode(data)

                await self.send(msg)
            
            elif msg.get_metadata("performative") == "INFO":
                coinid = data.coinid
                price = data.price
                volume = data.volume24h

                # Atualizar o preço
                if self.agent.portfolio[coinid].quantity is not None:
                    self.agent.portfolio[coinid].update(price)

            elif msg.get_metadata("performative") == "MAPREPLY":
                # Se não estiver no portfólio então compra
                coinid = data.coinid
                name = data.name

                if coinid not in self.agent.portfolio and coinid != "No matching coin found":
                    self.agent.portfolio[coinid] = Asset(coinid, name)

                    # Dar trigger a um agente collector e enviar mensagem ao broker pra comprar
                    collector = CollectorAgent(f"collector@{XMPP_SERVER}", PASSWORD)
                    collector.crypto = coinid

                    await collector.start(auto_register=True)

                    msg = Message(to="broker@localhost")
                    msg.set_metadata("performative", "BUY")

                    trade = Trade(coinid, balance=self.agent.trade_balance) # Balance deve vir da interface
                    msg.body = jsonpickle.encode(trade)

                    await self.send(msg)

            elif msg.get_metadata("performative") == "BUYREPLY":
                # RECEBE A QUANTIDADE DE TOKENS QUE COMPROU E A QUE PREÇO
                coinid = data.coinid

                self.agent.portfolio[coinid].set_info(data.price, data.quantity)

            elif msg.get_metadata("performative") == "SELLREPLY":
                coinid = data.coinid
                self.agent.balance += data.balance

                del self.agent.portfolio[coinid]

        else:
            print(f"{str(self.agent.jid).partition('@')[0]} : message timeout after 10 seconds")