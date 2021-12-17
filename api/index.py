from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from app.app import blueprint
from db import updateDB

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(
    id="Update db",
    func=updateDB,
    trigger="cron",
    hour="9",
    minute="0",
    second="0",
)
scheduler.start()


app.register_blueprint(blueprint)
app.run()
