from flask import Flask
from google.cloud import datastore

from flask_cors import CORS
import logging

from .blueprint import blueprint as api


logging.basicConfig(
    level=logging.INFO
)

app = Flask('Aggregator Service')
app.register_blueprint(api, url_prefix='/api')
app.datastore = datastore.Client()
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def root():
    return 'Aggregator Service'


app.logger.info(f'Service initialized successfully with environment')
