from flask import Flask, jsonify
from dicionario import dict_to_string

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello Cesar"

@app.route("/ola/<name>")
def Ola(name):
    return f"Ola, {name}!"

@app.route('/dicionario')
def get_dicionario():
    meu_dicionario = {
        'nome': 'Joao',
        'idade': 30,
        'cidade': 'Sao Paulo'
    }
    resultado = dict_to_string(meu_dicionario)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)