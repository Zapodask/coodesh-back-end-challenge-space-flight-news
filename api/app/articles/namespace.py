from flask_restx import Namespace, Resource, fields
from flask import request

from db import articles as db


articles = Namespace("articles", description="Articles operations")

launches_model = articles.model(
    "Launches",
    {
        "id": fields.String,
        "provider": fields.String,
    },
)

events_model = articles.model(
    "Events",
    {
        "id": fields.String,
        "provider": fields.String,
    },
)

model = articles.model(
    "Article",
    {
        "id": fields.String,
        "featured": fields.Boolean,
        "title": fields.String,
        "url": fields.String,
        "imageUrl": fields.String,
        "newsSite": fields.String,
        "summary": fields.String,
        "publishedAt": fields.String,
        "launches": fields.List(fields.Nested(launches_model)),
        "events": fields.List(fields.Nested(events_model)),
    },
)


@articles.route("/")
class Index(Resource):
    @articles.doc("list articles")
    @articles.marshal_list_with(model)
    def get(self):
        headers = request.headers

        limit = headers.get("limit")
        if limit == None:
            limit = 10
        else:
            limit = int(limit)

        page = headers.get("page")
        if page == None:
            page = 1
        else:
            page = int(page)

        res = db.find().limit(limit).skip((page - 1) * limit).sort("_id", -1)

        items = []
        for item in res:
            del item["_id"]
            items.append(item)

        return items, 200

    @articles.doc("create article")
    def post(self):
        req = request.get_json()

        last = db.find().limit(1).sort("_id", -1)
        last_id = last[0]["id"]

        req["id"] = int(last_id) + 1

        db.insert_one(req)

        return {"message": "Article created"}, 200


@articles.route("/<int:id>")
@articles.param("id", "Identifier")
@articles.response(404, "User not found")
class Id(Resource):
    @articles.doc("Show article")
    @articles.marshal_with(model)
    def get(self, id):
        article = db.find_one({"id": id})

        if article != None:
            del article["_id"]

            return article, 200
        else:
            return articles.abort(400, f"Article {id} not found")

    @articles.doc("Update article")
    def put(self, id):
        req = request.get_json()

        article = db.find_one({"id": id})

        if article != None:
            db.update_one({"id": id}, {"$set": req})

            return {"message": f"Article {id} updated"}, 200
        else:
            return {"message": f"Article {id} not found"}, 400

    @articles.doc("Delete article")
    def delete(self, id):
        article = db.find_one({"id": id})

        if article != None:
            db.delete_one({"id": id})

            return {"message": f"Article {id} deleted"}, 200
        else:
            return {"message": f"Article {id} not found"}, 400
