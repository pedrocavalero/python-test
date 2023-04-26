def dict_to_string(dicionario):
    lista = [f"{chave}: {valor}" for chave, valor in dicionario.items()]
    resultado = ", ".join(lista)
    return resultado

meu_dicionario = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

string_resultado = dict_to_string(meu_dicionario)
print(string_resultado)

from flask import Flask, jsonify

app = Flask(__name__)

meu_dicionario = {
    'nome': 'Joao',
    'idade': 30,
    'cidade': 'Sao Paulo'
}

@app.route('/dicionario')
def get_dicionario():
    
    resultado = dict_to_string(meu_dicionario)
    return jsonify(resultado)


