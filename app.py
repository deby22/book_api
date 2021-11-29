from flask import Flask, jsonify
from flask_restx import Api, Resource


app = Flask(__name__)

api = Api(app)


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
