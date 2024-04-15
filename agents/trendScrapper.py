from spade.agent import Agent
from behaviours.scrapeTrendBehav import scrapeTrendBehaviour

class TrendScrapperAgent(Agent):
    cryptos = ["crypto1", "crypto2", "crypto3", "crypto4", "crypto5", "crypto6", "crypto7"]
    async def setup(self):
        print("Trend's scrapper agent starting...")

        scraperBehav = scrapeTrendBehaviour(period=1)
        self.add_behaviour(scraperBehav)