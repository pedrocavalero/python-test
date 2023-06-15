from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

DVD_DB = []
NEXT_ID = 1

# Rota para obter todos os DVDs
@app.route('/dvds', methods=['GET'])
def get_all_dvds():
    return jsonify(DVD_DB)

# Rota para obter um DVD pelo ID
@app.route('/dvds/<int:dvd_id>', methods=['GET'])
def get_dvd_by_id(dvd_id):
    dvd = next((d for d in DVD_DB if d['id'] == dvd_id), None)
    return jsonify(dvd) if dvd else jsonify({'error': 'DVD not found'}), 404

# Rota para adicionar um DVD
@app.route('/dvds', methods=['POST'])
def create_dvd():
    dvd_data = request.get_json()
    nome = dvd_data.get('nome')
    ano_lancamento = dvd_data.get('ano_lancamento')
    
    dvd = {
        'id': len (DVD_DB),
        'nome': nome,
        'ano_lancamento': ano_lancamento
    }
    
    DVD_DB.append(dvd)
    return jsonify(dvd), 201

# Rota para atualizar um DVD pelo ID
@app.route('/dvds/<int:dvd_id>', methods=['PUT'])
def update_dvd(dvd_id):
    dvd = next((d for d in DVD_DB if d['id'] == dvd_id), None)
    if not dvd:
        return jsonify({'error': 'DVD not found'}), 404

    dvd_data = request.get_json()
    nome = dvd_data.get('nome')
    ano_lancamento = dvd_data.get('ano_lancamento')

    dvd['nome'] = nome
    dvd['ano_lancamento'] = ano_lancamento

    return jsonify(dvd)

# Rota para deletar um DVD pelo ID
@app.route('/dvds/<int:dvd_id>', methods=['DELETE'])
def delete_dvd(dvd_id):
    DVD_DB = [d for d in DVD_DB if d['id'] != dvd_id]
    return '', 204


def adicionar_dvd(nome, ano_lancamento):
    url = 'http://localhost:5000/dvds'
    payload = {'nome': nome, 'ano_lancamento': ano_lancamento}
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        dvd = response.json()
        print(f"DVD adicionado com sucesso! ID: {dvd['id']}, Nome: {dvd['nome']}, Ano de Lançamento: {dvd['ano_lancamento']}")
    else:
        print("Erro ao adicionar o DVD")

if __name__ == '__main__':
     app.run(debug=True)
