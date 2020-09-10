from flask import Flask

app = Flask(__name__)


def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db


def add_country(db):
    db.countries.drop()
    db.countries.insert_one({"name": "Bulgaria"})
    db.countries.insert_one({"name": "Germany"})
    db.countries.insert_one({"name": "USA"})
    db.countries.insert_one({"name": "Canada"})


def get_country(db):
    return db.countries.find_one()


def get_countries(db):
    return db.countries.find()


@app.route("/")
def hello():
    db = get_db()
    add_country(db)
    result = ''
    for country in get_countries(db):
        result += "<h3>" + str(country) + "</h3>"
    return result


if __name__ == "__main__":
    app.run()
