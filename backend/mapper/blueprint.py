from flask import Blueprint
from flask_restx import Api
from .api import api


blueprint = Blueprint('api', 'Custom Dialog Engine API')

api = Api(
    version='0.0',
    title='Data Table Aggregation API',
    description='Handles Aggregations and additions for data tables per Zero NLP interview task specifications',
    validate=True
)
api.init_app(blueprint)
api.add_namespace(api)

# TODO: error handler for open AI errors


@api.errorhandler
def default_error_handler(error):
    '''Default error handler'''
    return {
        'message': 'An unexpected error occurred',
        'internal_message': str(error)
    }, getattr(error, 'code', 500)