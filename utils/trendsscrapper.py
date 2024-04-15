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
                # Omit unnecessary headers to avoid raising flags
                "User-Agent": "Mozilla/5.0 (Python; Trends Scraper)",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            },
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



