from flask import Flask, jsonify
from twitter.scraper import Scraper
from datetime import datetime

## sign-in with credentials
scraper = Scraper("guilherme.lukon@gmail.com", "randommeme65920", "projetoasm123")
app = Flask(__name__)

@app.route('/tweets/<user>')
def get_tweets(user):
    users = scraper.users([user])
    userid = users[0]["data"]["user"]["result"]["rest_id"]
    tweets = scraper.tweets([userid], limit=1)
    
    entries = None
    for timeline in tweets[0]["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"]:
        if timeline["type"] == "TimelineAddEntries":
            entries = timeline

    text = entries["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]
    date = datetime.strptime(entries["entries"][0]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["created_at"], '%a %b %d %H:%M:%S %z %Y')

    tweet = {"text": text, "date": date}
    return jsonify(tweet)

@app.route('/trends')
def get_trends():
    trends = scraper.trends()
    return jsonify(trends)


if __name__ == '__main__':
    app.run(debug=True)
