from flask import Flask

from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

import models  # noqa: E402,F401  (table register होण्यासाठी)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Hello, Expense Tracker!"


if __name__ == "__main__":
    app.run(debug=True)