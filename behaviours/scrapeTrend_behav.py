from spade.behaviour import PeriodicBehaviour
from utils.trendsscrapper import TrendScraper
from spade.message import Message
import random
import jsonpickle

class ScrapeTrendBehaviour(PeriodicBehaviour):
    async def run(self):
        print("Trend's scraper behaviour running...")
        cryptos  = random.sample(self.agent.cryptos,3)
        scraper = TrendScraper()
        trending_topics = scraper.trends()
        
        for item in cryptos:
            i = random.randint(0, len(trending_topics))
            trending_topics.insert(i, item)
        
        msg = Message(to="manager@localhost") # Enviar ao manager?
        msg.set_metadata("performative", "trends")
        msg.body = jsonpickle.encode(trending_topics)
        
        print(f"{self.agent.jid}: Sending trending topics to manager - {trending_topics}")
        
        await self.send(msg)

        
        