from agents import trendScrapper
from spade import quit_spade
import time

if __name__ == "__main__":
    trendScrapper = trendScrapper.TrendScrapperAgent("trendscrapper_agent@mi", "admin")
    future = trendScrapper.start()
    future.result()

    while trendScrapper.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            trendScrapper.stop()
            break

    quit_spade()

