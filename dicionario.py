def dict_to_string(dicionario):
    lista = [f"{chave}: {valor}" for chave, valor in dicionario.items()]
    resultado = ", ".join(lista)
    return resultado



from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dicionario')
def get_dicionario():
    meu_dicionario = {
        'nome': 'Joao',
        'idade': 30,
        'cidade': 'Sao Paulo'
    }
    resultado = dict_to_string(meu_dicionario)
    return jsonify(resultado)


