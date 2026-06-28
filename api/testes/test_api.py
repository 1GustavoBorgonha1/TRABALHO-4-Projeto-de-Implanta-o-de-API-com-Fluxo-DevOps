import sys #Acessa configurações do python durante a execução
import os
#Busca a pasta onde esta o app.py e adiciona ela na posição principal (0)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
#Importa framework de testes, econtrando funções automaticamente quando começam com _test, executalas e verificar os assest, depois retorna os resultados
import pytest 
#Importa o objeto app que criei em app.py
from app import app

@pytest.fixture # Indica ao pytest que esta função prepara o ambiente antes de cada teste
def client():
    app.config["TESTING"] = True # Ativa o modo de testes no Flask, passando os erros para o pytest
    with app.test_client() as client: #Cria um cliente que simula as requisições, sem subir um servidor real
        yield client #Retorna o cliente e encerra a conexão no fim

#Teste de estrutura do json da rota de clientes
def test_estrutura_json_pacientes(client):
    resposta = client.get("/pacientes")
    dados = resposta.get_json()
    campos_obrigatorios = {"id", "nome", "especie", "raca", "idade", "peso_kg", "tutor", "status"}
    for campo in campos_obrigatorios:
        assert campo in dados["data"][0]

#Testa se a rota pacientes esta disponivel (200)
def test_get_pacientes_retorna_200(client):
    resposta = client.get("/pacientes")
    assert resposta.status_code == 200

#Testa se a rota clientes retorna 404 quando buscamos um id que não existe
def test_paciente_inexistente_retorna_404(client):
    resposta = client.get("/pacientes/989898")
    assert resposta.status_code == 404

#Criação prórpria.Testa se a rota status esta disponivel (200) e se retorna todos os campos
def test_status_retorna_campos_esperados(client):
    resposta = client.get("/status")
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert "nome" in dados["data"]
    assert "versao" in dados["data"]
    assert "status" in dados["data"]