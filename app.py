from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for


from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

import models 
from models import Transaction 

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Hello, Expense Tracker!"
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = float(request.form["amount"])
        tx_type = request.form["type"]
        tx_date = datetime.strptime(request.form["date"], "%Y-%m-%d").date()
        note = request.form["note"]

        tx = Transaction(amount=amount, type=tx_type, date=tx_date, note=note)
        db.session.add(tx)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add_transaction.html")


if __name__ == "__main__":
    app.run(debug=True)