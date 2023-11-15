#basic flask application
from flask import Flask
from config import Config
from .blueprints.site.routes import site

#instantiating our Flask app
app = Flask(__name__) #passing in the __name__ variable which just takes the name of the folder we're in
app.config.from_object(Config)

# #we are going to use a decorator to create our first route
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!<p>"

app.register_blueprint(site) #add this here to register your site blueprint