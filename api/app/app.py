from flask import Blueprint
from flask_restx import Api, Resource

from .articles.namespace import articles as articleNamespace


blueprint = Blueprint("api", __name__, url_prefix="/v1")
api = Api(
    blueprint,
    version="1.0",
    title="Articles api",
    description="A simple TODO API",
)


api.add_namespace(articleNamespace)


@api.route("/")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Back-end challenge 2021 - Space Flight News"}, 200
