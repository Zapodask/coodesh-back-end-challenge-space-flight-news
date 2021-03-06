from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

import requests
import json


load_dotenv()

client = MongoClient(getenv("CLUSTER"))

db = client["spacedb"]

articles = db["articles"]


def updateDB():
    print("Updating DB")

    to_add = []
    n = 0
    loop = True
    last_id = int((articles.find().limit(1).sort("_id", -1))[0]["id"])

    while loop:
        res = requests.get(
            f"https://api.spaceflightnewsapi.net/v3/articles?_start={n * 10}"
        )
        text = json.loads(res.text)

        for item in list(text):
            article = articles.find_one({"title": item.get("title")})

            if article == None:
                last_id += 1
                item["id"] = str(last_id)
                to_add.append(item)
                print(f'Appending: {item.get("title")}')
            else:
                tal = len(to_add)

                if tal != 0:
                    print(f"{tal} articles to add")

                    articles.insert_many(to_add)

                    print("Articles added")
                else:
                    print("No articles to add")

                loop = False
                break

        n += 1
