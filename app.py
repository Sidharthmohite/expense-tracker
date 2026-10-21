from flask import Flask
from sqlalchemy import true
app = Flask (__name__ )


@app.route("/")
def home():
    return "welcome to the expense tracker app"
if __name__ == '__main__':
    app.run(debug=True)

