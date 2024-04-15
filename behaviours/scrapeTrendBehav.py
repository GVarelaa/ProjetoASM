from spade.behaviour import PeriodicBehaviour
from utils.trendsscrapper import TrendScraper
#from spade.message import Message
import random

class scrapeTrendBehaviour(PeriodicBehaviour):
    async def run(self):
        print("Trend's scraper behaviour running...")
        cryptos  = random.sample(self.agent.cryptos,3)
        scraper = TrendScraper()
        trending_topics = scraper.trends()
        print("TTs: ", trending_topics)
        
        for item in cryptos:
            i = random.randint(0, len(trending_topics))
            trending_topics.insert(i, item)
        print("Final List: ", trending_topics)


        
        