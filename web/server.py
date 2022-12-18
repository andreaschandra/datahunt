"""Web server datahunt"""
from flask import Flask, request, jsonify, render_template
from db_connection import get_connection, get_data
from util import generate_answer_query

conn, cursor = get_connection()

app = Flask(__name__)


@app.route("/")
def homepage():
    return jsonify("The server is on")


@app.route("/checkdata", methods=["GET", "POST"])
def checkdata():
    if request.method == "GET":
        return jsonify({"message": "Ahh! You should send POST"})
    else:
        content = request.json
        input_query = content["query"]
        exercise = content["exercise"]
        answer_query = generate_answer_query(exercise)

        user_col, user_data = get_data(input_query)
        answer_col, answer_data = get_data(answer_query)

        if (user_col == answer_col) & (user_data == answer_data):
            return jsonify("True")
        else:
            return jsonify("False")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
