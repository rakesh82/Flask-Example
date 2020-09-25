###
#   headlines.py - simple app for getting the news headlines
###

# importing required library
import feedparser
from flask import Flask
from flask import render_template
from flask import request

# creating flask object
app = Flask(__name__)

# creating dictionary of feeds
RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
}


# routing
@app.route("/", methods=['GET', 'POST'])
# get_news function to be called
def get_news():
    # fetching publication argument
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", news=publication.upper(), articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
