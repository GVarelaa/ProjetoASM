import requests
import re
import jsonpickle
from datetime import datetime
from spade.behaviour import PeriodicBehaviour
from spade.message import Message

class CallerBehaviour(PeriodicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        response = requests.get(f'http://127.0.0.1:5000/tweets/{self.agent.user}')

        if response.status_code == 200:
            data = response.json()

            date1 = datetime.strptime(data["date"], "%a, %d %b %Y %H:%M:%S GMT")

            if "date" in self.agent.last_tweet:
                date2 = datetime.strptime(self.agent.last_tweet["date"], "%a, %d %b %Y %H:%M:%S GMT")
            else:
                date2 = None

            if date2 is None or date1 > date2:
                self.agent.last_tweet["tweet"] = data["text"]
                self.agent.last_tweet["date"] = data["date"]

                match = re.search(r'\$\w+\b', data["text"])

                if match is not None:
                    msg = Message(to="manager@localhost")
                    msg.set_metadata("performative", "CALL")
                    
                    msg.body = jsonpickle.encode({"ticker": match.group(0)})

                    await self.send(msg)
                else:
                    print("Ticker not found")
        else:
            print('Request error:', response.status_code)