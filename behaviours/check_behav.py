import jsonpickle
from spade.behaviour import PeriodicBehaviour
from spade.message import Message
from utils.trade import Trade

class CheckBehaviour(PeriodicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"Portfolio : {self.agent.portfolio}")

        for coinid in self.agent.portfolio:
            coin = self.agent.portfolio[coinid]
            print(coin)

            if coin.profit >= self.agent.takeprofit:
                # Vender 
                msg = Message(to="broker@localhost")
                msg.set_metadata("performative", "SELL")

                trade = Trade(coinid, quantity=coin.quantity)

                msg.body = jsonpickle.encode(trade)

            elif coin.profit <= self.agent.stoploss:
                # Vender
                msg = Message(to="broker@localhost")
                msg.set_metadata("performative", "SELL")

                trade = Trade(coinid, quantity=coin.quantity)

                msg.body = jsonpickle.encode(trade)
