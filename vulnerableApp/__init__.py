from flask import Flask

app = Flask(__name__)

from vulnerableApp import routes
