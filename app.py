from flask import Flask, jsonify
from dicionario import dict_to_string
from flask import Flask, jsonify
from dicionario import dict_to_string

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello Cesar"

if __name__ == '__main__':
    app.run(debug=True)