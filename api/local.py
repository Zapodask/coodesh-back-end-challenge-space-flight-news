from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import time

from app.app import blueprint


def updateDB():
    print("Updating")
    time.sleep(10)
    print("Updated")


app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(
    id="Update db",
    func=updateDB,
    trigger="cron",
    hour="17",
    minute="0",
    second="0",
)
scheduler.start()

app.register_blueprint(blueprint)
app.run(debug=True)
