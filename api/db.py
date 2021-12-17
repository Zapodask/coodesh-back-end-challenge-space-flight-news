from pymongo import MongoClient
import requests
import json


client = MongoClient(
    "mongodb+srv://zapodask:zapodask@cluster0.kngaq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = client["spacedb"]

articles = db["articles"]


def updateDB():
    to_add = []
    n = 0
    loop = True

    while loop:
        res = requests.get(
            f"https://api.spaceflightnewsapi.net/v3/articles?_start={n * 10}"
        )
        text = json.loads(res.text)

        for item in list(text):
            article = articles.find_one({"title": item.get("title")})

            if article == None:
                to_add.append(item)
                print(f'Appending: {item.get("title")}')
            else:
                tal = len(to_add)

                if tal != 0:
                    print(f"{tal} articles to add")

                    articles.insert_many(to_add)
                else:
                    print("No articles to add")

                loop = False
                break

        n += 1
