from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/respond/<string>", methods=['GET'])
def analyse_sentiment(string: str):
    return jsonify(
        response=string
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
