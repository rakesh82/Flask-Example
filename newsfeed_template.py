###
#   newsfeed_template.py - multiple news feeds and uses of Jinja templates
###

import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

# Feeds channel
NEWS_FEED = {
    'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
    'cnn': "http://rss.cnn.com/rss/edition.rss",
    'fox': "http://feeds.foxnews.com/foxnews/latest",
    'iol': "http://www.iol.co.za/cmlink/1.640"
}


# routing
@app.route("/")
@app.route("/<publication>")
# functions
def get_news(publication='bbc'):
    feed = feedparser.parse(NEWS_FEED[publication])
    #first_article = feed['entries'][0]
    return render_template("home.html",
                           news=publication.upper(), articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
