from flask import Flask, jsonify, request
from itens import itens
from dicionario import dict_to_string
from dotenv import load_dotenv
import os
import requests

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


@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}!"


@app.route('/dicionario')
def get_dicionario():
    meu_dicionario = {
        'nome': 'Joao',
        'idade': 30,
        'cidade': 'Sao Paulo'
    }
    resultado = dict_to_string(meu_dicionario)
    return jsonify(resultado)

load_dotenv()

def obter_noticias():
    api_key = os.getenv('API_KEY')
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'br',
        'apiKey': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        articles = data['articles']
        news = []
        for article in articles:
            title = article['title']
            source = article['source']['name']
            news.append(f'Título: {title} | Fonte: {source}')
        return news
    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {str(e)}')
        return []

@app.route('/noticias')
def get_noticias():
    noticias = obter_noticias()
    if noticias:
        return jsonify({'noticias': noticias})
    else:
        return jsonify({'mensagem': 'Não foi possível obter as notícias.'})

if __name__ == '__main__':
     app.run(debug=True)