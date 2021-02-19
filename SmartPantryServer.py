from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/item')
def display_item():
    item = [{
        "Item": "Banana",
        "Category": "Fruit",
    }]
    
    response = app.response_class(
        response=json.dumps(item),
        status=200,
        mimetype='application/json'
    )
    return jsonify(response)


if __name__ == '__main__':
   app.run(host='0.0.0.0')
