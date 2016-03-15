from flask import Flask, jsonify, abort, make_response, request
from dao import tarefas_dao
from dao import helper
from tarefas import Tarefas
from datetime import datetime
import json


app = Flask(__name__)

_tarefas = Tarefas()
_dao = tarefas_dao.TarefasDao()
_helper = helper.DaoHelper()

_helper.criarTabelas()

empresas = [
    {"nome" : "Turis Thermas"},
    {"nome" : "AVN"},
    {"nome" : "Turis Thermas"},
    {"nome" : "Thermas e Cia"},
    {"nome" : "Lagoa Quente"},
    {"nome" : "Thermas Tour"},
    {"nome" : "AquaThermas"},
    {"nome" : "Grupo Privé"},
    {"nome" : "Caldas Vip"},
    {"nome" : "Magic City"},
    {"nome" : "Icconne Hoteis"},
    {"nome" : "Le Jardin"},
    {"nome" : "SnowLand"},
    {"nome" : "Cacoal"},
    {"nome" : "Cascaneia"},
    {"nome" : "Viaje Bem Brasil"},
    {"nome" : "Portugal Viagens"}
]


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route('/service/api/tarefas', methods=['GET', 'OPTIONS'])
def retrieve_tarefas():

   tarefasList = _dao.retornaTodos()

   return json.dumps(tarefasList)


@app.route('/service/api/empresas', methods=['GET'])
def retrieve_empresas():
    return json.dumps(empresas)


@app.route('/service/api/<int:id>', methods=['GET'])
def by_id(id):

    return


@app.route('/service/api/add', methods=['POST'])
def add():
    if not request.json:
        abort(404)

    titulo = request.json['titulo']
    descricao = request.json['descricao']
    data = str(datetime.now())
    print(data)
    # data = str(datetime.date(datetime.now()))
    empresa = request.json['empresa']
    print(empresa['nome'])

    _tarefas.titulo = titulo
    _tarefas.descricao = descricao
    _tarefas.data = data
    _tarefas.empresa = empresa['nome']
    print(_tarefas.empresa)
    _dao.cadastrar(_tarefas)


    return jsonify({'response' : 'Cadastrado com sucesso!'})


@app.route('/service/api/update/<int:id>', methods=['PUT'])
def update(id):
    if not request.json or id <= 0:
        abort(404)

    return jsonify({'response' : 'Url indisponivel'})


@app.route('/service/api/delete', methods=['POST'])
def delete():
    if not request.json:
        abort(404)

    lista = request.json
    print(lista)

    for i in range(len(lista)):
        id = lista[i]['id']
        _dao.deletar(id)

    return jsonify({'response' : 'Url indisponivel'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run(port=8080, debug=True)