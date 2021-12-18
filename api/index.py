from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from werkzeug.middleware.proxy_fix import ProxyFix

from app.app import blueprint
from db import updateDB

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(blueprint)

if __name__ == "__main__":
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

    app.run()
