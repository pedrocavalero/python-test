from flask import Flask, jsonify, request
from itens import itens

app = Flask(__name__)

@app.route('/lista')
def lista():
    lista=['maca', 'macaco', 'chuchu']
    return lista

@app.route('/itens')
def get_itens():
    cor = request.args.get('cor')
    tamanho = request.args.get('tamanho')
    itens_filtrados = [item for item in itens if (cor is None or item['cor'] == cor) and (tamanho is None or item['tamanho'] == tamanho)]
    return jsonify(itens_filtrados)


@app.route('/concatenar')
def concatenar():
    parametros = request.args.getlist('parametro')
    lista_parametros = list(parametros)
    string_concatenada = ''
    for parametro in lista_parametros:
        string_concatenada += parametro + '-'

    string_concatenada = string_concatenada[:-1]

    return f'A lista de parâmetros é: {lista_parametros}. A string concatenada é: {string_concatenada}.'


if __name__ == '__main__':
    app.run(debug=True)