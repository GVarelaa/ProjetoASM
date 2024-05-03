from spade.behaviour import PeriodicBehaviour
from utils.crypto_info import get_market_data
from utils.data import Data
from spade.message import Message
import jsonpickle

class CollectBehaviour(PeriodicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        msg = Message(to="manager@localhost")
        msg.set_metadata("performative", "INFO")

        data = get_market_data(self.agent.crypto)

        coinid = data["id"]
        name = data["name"]
        price = data["quote"]["USD"]["price"]
        volume = data["quote"]["USD"]["volume_24h"]
        marketcap = data["quote"]["USD"]["market_cap"]

        msg.body = jsonpickle.encode(Data(coinid, name, price, volume, marketcap))

        await self.send(msg)