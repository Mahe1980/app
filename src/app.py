from flask import Flask, jsonify

app = Flask(__name__)


def sum_range(start, end):
    return (end * (end + 1) / 2) - (start - 1) * start / 2


@app.route("/total")
def total():
    numbers_to_add = list(range(10000001))
    return jsonify(total=sum_range(numbers_to_add[0], numbers_to_add[-1]))


if __name__ == "__main__":
    app.run()
