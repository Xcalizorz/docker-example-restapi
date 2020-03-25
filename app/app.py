from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/respond/<string>", methods=['GET'])
def simple_response(string: str):
    return jsonify(
        response=string
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
