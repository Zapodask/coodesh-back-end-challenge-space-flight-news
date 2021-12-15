from flask_restx import Namespace, Resource, fields


articles = Namespace("articles", description="Articles operations")

model = articles.model(
    "Article",
    {
        "id": fields.Integer,
        "featured": fields.Boolean,
        "title": fields.String,
        "url": fields.String,
        "imageUrl": fields.String,
        "newsSite": fields.String,
        "summary": fields.String,
        "publishedAt": fields.String,
        "launches": [{"id": fields.String, "provider": fields.String}],
        "events": [{"id": fields.String, "provider": fields.String}],
    },
)


@articles.route("/")
class Index(Resource):
    @articles.doc("list articles")
    # @articles.marshal_list_with(model)
    def get(self):
        return {"message": "Ok"}, 200

    @articles.doc("create article")
    def post(self):
        return {"message": "Ok"}, 200


@articles.route("/<int:id>")
@articles.param("id", "Identifier")
@articles.response(404, "User not found")
class Id(Resource):
    @articles.doc("Show article")
    @articles.marshal_with(model)
    def get(self, id):
        return {"message": f"Ok {id}"}, 200

    @articles.doc("Update article")
    @articles.marshal_with(model)
    def put(self, id):
        return {"message": f"Ok {id}"}, 200

    @articles.doc("Delete article")
    @articles.marshal_with(model)
    def delete(self, id):
        return {"message": f"Ok {id}"}, 200
