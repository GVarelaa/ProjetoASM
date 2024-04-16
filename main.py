#from agents import trendScrapper
from agents.pricer import PricerAgent
from spade import quit_spade
import time

if __name__ == "__main__":
    """
    trendScrapper = trendScrapper.TrendScrapperAgent("trendscrapper_agent@mi", "admin")
    future = trendScrapper.start()
    future.result()

    while trendScrapper.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            trendScrapper.stop()
            break
    """

    pricer_agent = PricerAgent("pricer_agent@zenbookum5401qa", "admin")
    future = pricer_agent.start()
    future.result()

    while pricer_agent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            pricer_agent.stop()
            break

    quit_spade()

