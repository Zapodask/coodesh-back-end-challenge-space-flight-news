import json
import requests

from api.db import articles

to_add = []
n = 0
loop = True

while loop:
    res = requests.get(
        f"https://api.spaceflightnewsapi.net/v3/articles?_limit=500&_sort=id&_start={n * 500}"
    )

    text = json.loads(res.text)

    for item in list(text):
        to_add.append(item)

    if text == []:
        articles.insert_many(to_add)

    n += 1
