from twitter.scraper import Scraper
from datetime import datetime

## sign-in with credentials
email, username, password = "guilherme.lukon@gmail.com", "randommeme65920", "projetoasm123"
scraper = Scraper(email, username, password)

#trends = scraper.trends()

#print(trends)


#users = scraper.users(['MacnBTC'])

#print(users)

tweets = scraper.tweets(['996294856078188544'], limit=10)

#print(tweets[0]["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"])

obj = None
for timeline in tweets[0]["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"]:
    if timeline["type"] == "TimelineAddEntries":
        obj = timeline

print(obj["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"])
date = obj["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["created_at"]

formato = '%a %b %d %H:%M:%S %z %Y'

datetime = datetime.strptime(date, formato)
print(datetime)