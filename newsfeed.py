###
#   newsfeed.py - application for news feeds from multiple sites
###

import feedparser
from flask import Flask

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
    first_article = feed['entries'][0]
    return """<html>
                <body>
                    <h1>{0} News</h1>
                    <b>{1}</b></br>
                    <i>{2}</i></br>
                    <p>{3}</p> <br/>
                </body>""".format(publication.upper(), first_article.get('title'), first_article.get("published"),
                                  first_article.get("summary"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
