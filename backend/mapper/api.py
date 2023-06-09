from flask_restx import Api, Resource, fields
import logging

# Create the API
api = Api(
    version="1.0",
    title="Aggregations and Additions API",
    description="A simple API for managing aggregations and additions",
)

# Create the API models
aggregation_model = api.model(
    "Aggregation",
    {
        "aggregation_id": fields.Integer(required=True, description="The aggregation identifier"),
        "name": fields.String(required=True, description="The aggregation name"),
    },
)

addition_model = api.model(
    "Addition",
    {
        "addition_id": fields.Integer(required=True, description="The addition identifier"),
        "name": fields.String(required=True, description="The addition name"),
    },
)

# Create the Aggregations endpoints
@api.route("/aggregations")
class Aggregations(Resource):
    """
    Endpoint for managing aggregations
    """

    @api.doc("list_aggregations")
    @api.marshal_list_with(aggregation_model)
    def get(self):
        """
        List all aggregations
        """
        logging.info("Listing all aggregations")
        return []

    @api.doc("create_aggregation")
    @api.expect(aggregation_model)
    @api.marshal_with(aggregation_model, code=201)
    def post(self):
        """
        Create a new aggregation
        """
        logging.info("Creating a new aggregation")
        return {}

@api.route("/aggregations/<aggregation_id>")
@api.param("aggregation_id", "The aggregation identifier")
class Aggregation(Resource):
    """
    Endpoint for managing a single aggregation
    """

    @api.doc("get_aggregation")
    @api.marshal_with(aggregation_model)
    def get(self, aggregation_id):
        """
        Get a single aggregation
        """
        logging.info("Getting aggregation %s", aggregation_id)
        return {}

    @api.doc("update_aggregation")
    @api.expect(aggregation_model)
    @api.marshal_with(aggregation_model)
    def put(self, aggregation_id):
        """
        Update an aggregation
        """
        logging.info("Updating aggregation %s", aggregation_id)
        return {}

    @api.doc("delete_aggregation")
    @api.marshal_with(aggregation_model)
    def delete(self, aggregation_id):
        """
        Delete an aggregation
        """
        logging.info("Deleting aggregation %s", aggregation_id)
        return {}

# Create the Additions endpoints
@api.route("/aggregations/<aggregation_id>/additions")
@api.param("aggregation_id", "The aggregation identifier")
class Additions(Resource):
    """
    Endpoint for managing additions
    """

    @api.doc("list_additions")
    @api.marshal_list_with(addition_model)
    def get(self, aggregation_id):
        """
        List all additions for an aggregation
        """
        logging.info("Listing all additions for aggregation %s", aggregation_id)
        return []

    @api.doc("create_addition")
    @api.expect(addition_model)
    @api.marshal_with(addition_model, code=201)
    def post(self, aggregation_id):
        """
        Create a new addition for an aggregation
        """
        logging.info("Creating a new addition for aggregation %s", aggregation_id)
        return {}

@api.route("/aggregations/<aggregation_id>/additions/<addition_id>")
@api.param("aggregation_id", "The aggregation identifier")
@api.param("addition_id", "The addition identifier")
class Addition(Resource):
    """
    Endpoint for managing a single addition
    """

    @api.doc("get_addition")
    @api.marshal_with(addition_model)
    def get(self, aggregation_id, addition_id):
        """
        Get a single addition
        """
        logging.info("Getting addition %s for aggregation %s", addition_id, aggregation_id)
        return {}

    @api.doc("update_addition")
    @api.expect(addition_model)
    @api.marshal_with(addition_model)
    def put(self, aggregation_id, addition_id):
        """
        Update an addition
        """
        logging.info("Updating addition %s for aggregation %s", addition_id, aggregation_id)
        return {}

    @api.doc("delete_addition")
    @api.marshal_with(addition_model)
    def delete(self, aggregation_id, addition_id):
        """
        Delete an addition
        """
        logging.info("Deleting addition %s for aggregation %s", addition_id, aggregation_id)
        return {}