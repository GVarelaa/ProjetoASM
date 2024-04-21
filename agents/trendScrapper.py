from spade.agent import Agent
from behaviours.scrapeTrend_behav import ScrapeTrendBehaviour

class TrendScrapperAgent(Agent):
    cryptos = ["crypto1", "crypto2", "crypto3", "crypto4", "crypto5", "crypto6", "crypto7"]
    async def setup(self):
        print("Trend's scrapper agent starting...")

        scraperBehav = ScrapeTrendBehaviour(period=1)
        self.add_behaviour(scraperBehav)