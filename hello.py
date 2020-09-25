####
##      hello.py - Creating first webservice
####

# Importing the flask
from flask import Flask

# creating instance of flask object
# flask uses package name - so always take __name__
app = Flask(__name__)


# flask uses decorator for URL routing
# / - denotes the root page of application
@app.route("/")

# index() - used for returning the message
def index():
    return "Hello Wold!"


if __name__ == '__main__':
    #
    app.run(port=5000, debug=True)
