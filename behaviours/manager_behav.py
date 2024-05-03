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
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")
        
        msg = await self.receive(timeout=10)

        if msg:
            data = jsonpickle.decode(msg.body)
            
            print(f"{str(self.agent.jid).partition('@')[0]} : message received with content: " + str(data))

            if msg.get_metadata("performative") == "CALL":
                msg = Message(to="mapper@localhost")
                msg.set_metadata("performative", "MAP")
                msg.body = jsonpickle.encode(data)

                await self.send(msg)
            
            elif msg.get_metadata("performative") == "INFO":
                coinid = data["coinid"]
                price = data["quote"]["USD"]["price"]
                # volume = data["volume"]

                # Atualizar o preço
                self.agent.portfolio[coinid].update(price)

            elif msg.get_metadata("performative") == "MAPREPLY":
                # Se não estiver no portfólio então compra
                coinid = data.coinid

                if coinid not in self.agent.portfolio:
                    self.agent.portfolio[coinid] = Asset(coinid)

                    # Dar trigger a um agente collector e enviar mensagem ao broker pra comprar
                    collector = CollectorAgent(XMPP_SERVER, PASSWORD)
                    collector.crypto = coinid
                    collector.start(auto_register=True)

                    msg = Message(to="broker@localhost")
                    msg.set_metadata("performative", "BUY")

                    trade = Trade(coinid, 100) # Balance deve vir da interface
                    msg.body = jsonpickle.encode(trade)

            elif msg.get_metadata("performative", "BUYREPLY"):
                # RECEBE A QUANTIDADE DE TOKENS QUE COMPROU E A QUE PREÇO
                coinid = data.coinid

                self.agent.portfolio[coinid].set_info(data.price, data.quantity)

            elif msg.get_metadata("performative", "SELLREPLY"):
                coinid = data.coinid
                self.agent.balance += data.balance

                del self.agent.portfolio[coinid]

        else:
            print(f"{str(self.agent.jid).partition('@')[0]} : message timeout after 10 seconds")