from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import requests
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    response = requests.get("https://laptop-friendly.onrender.com/all")
    cafes = response.json()
    return render_template("index.html", cafes=cafes)


# with app.app_context():
#     result = db.session.execute(db.select(Cafe))
#     all_cafes = result.scalars().all()
#     for cafe in all_cafes:
#         params = {"loc": cafe.location}
response = requests.get("https://laptop-friendly.onrender.com/all")
data = response.json()


response = requests.get("https://laptop-friendly.onrender.com/all")
cafes = response.json()



@app.route("/")
def check():
    return render_template("index.html", cafes=cafes)


@app.route('/all_cafes')
def all_cafes():
    return render_template("about.html", cafes=cafes)


@app.route("/find/<int:cafe_id>", methods=["GET", "POST"])
def find_cafe(cafe_id):
    for cafe in cafes:
        if cafe["id"] == cafe_id:
            requested_c = cafe
            return render_template("contact.html", requested_c=requested_c)
    return render_template("about.html", cafes=cafes)


if __name__ == '__main__':
    app.run(debug=True)
