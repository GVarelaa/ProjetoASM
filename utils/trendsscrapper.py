import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime


class TrendScraper:
    """
    This class scrapes trending topics from trends24.in
    """

    def __init__(self):
        self.location = "in"
        self.page = "trends24"

    def trends(self):
        """
        Scrapes trending topics from the configured location and page.

        Returns:
            list: A list of strings containing the trending topics.
        """
        url = f"https://www.{self.page}.{self.location}/"
        req = urllib.request.Request(
            url,
            data=None,
            headers={
            #'authority': 'scrapeme.live',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            }
        )
        try:
            with urllib.request.urlopen(req) as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                rows = soup.find_all("li")
                trends = [row.get_text() for row in rows[:25]]
                return trends
        except Exception as e:
            print(f"Error scraping trends: {e}")
            return []



