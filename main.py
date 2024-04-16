#from agents import trendScrapper
from agents.collector import CollectorAgent
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

    collector_agent = CollectorAgent("collector_agent@zenbookum5401qa", "admin")
    future = collector_agent.start()
    future.result()

    while collector_agent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            collector_agent.stop()
            break

    quit_spade()

