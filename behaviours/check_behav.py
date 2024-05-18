import jsonpickle
from spade.behaviour import PeriodicBehaviour
from spade.message import Message
from utils.trade import Trade
from utils.log import Log

class CheckBehaviour(PeriodicBehaviour):
    async def on_start(self):
        Log.log(str(self.agent.jid).partition('@')[0], "starting check behaviour...")

    async def run(self):
        for coinid in self.agent.portfolio:
            coin = self.agent.portfolio[coinid]

            if coin.profit >= self.agent.takeprofit:
                # Vender 
                msg = Message(to="broker@localhost")
                msg.set_metadata("performative", "sell_request")

                trade = Trade(coinid, quantity=coin.quantity)

                msg.body = jsonpickle.encode(trade)

                await self.send(msg)

            elif coin.profit <= self.agent.stoploss*(-1):
                # Vender
                msg = Message(to="broker@localhost")
                msg.set_metadata("performative", "sell_request")

                trade = Trade(coinid, quantity=coin.quantity)

                msg.body = jsonpickle.encode(trade)

                await self.send(msg)
