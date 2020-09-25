###
#   headline.py - simple application for showing news headline, weather information, and currency exchange
###
# for parsing the RSS feeds
import feedparser

# importing the flask
from flask import Flask

# creating the flask object
app = Flask(__name__)

# creating feeds
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

# routing using decorator
@app.route("/")
# to get news feed
def get_news():
    # getting the news feed parse
    feeds = feedparser.parse(BBC_FEED)
    first_article = feeds['entries'][0]
    return """<html>
                <body>
                    <h1> BBC Headlines </h1>
                    <b>{0}</b></br>
                    <i>{1}</i></br>
                    <p>{2}</p> <br/>
                </body>""".format(first_article.get('title'), first_article.get("published"),
                                  first_article.get("summary"))


if __name__ == '__main__':
    # running the app
    app.run(port=5000, debug=True)
