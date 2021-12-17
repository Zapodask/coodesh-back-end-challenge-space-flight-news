from flask import Flask

from app.app import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
app.run(debug=True)
