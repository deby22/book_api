from flask import Flask, jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

import os

basedir = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "books.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db = SQLAlchemy(app)


@api.route("/books")
class Books(Resource):
    def get(self):
        return jsonify({"message": "Hello"})

    def post(self):
        pass


@api.route("/book/<int:id>")
class BookResource(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


if __name__ == "__main__":
    app.run(debug=True)
