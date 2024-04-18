import requests
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
            date2 = datetime.strptime(self.agent.last_tweet["date"], "%a, %d %b %Y %H:%M:%S GMT")

            if date1 > date2:
                # Fazer o processamento de linguagem com o $ e enviar a performative para comprar
                msg = Message(to="manager@localhost") # Enviar ao manager?
                msg.set_metadata("performative", "CALL")
        else:
            print('Request error:', response.status_code)
