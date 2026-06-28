import json # Serve para ler o Json
import os #Me da acesso a informações do SO, no caso vou usar para identificar caminhos de pastas
from flask import Flask, jsonify #Flask é a ferramenta para subir o servidor e o jsonify formata as respostas 

app = Flask(__name__) # Cria um servidor interno usando o Flask

#Função para buscar os dados dos pacientes
def carregar_pacientes():
    #Monta o caminho onde esta os dados dos pacientes
    caminho = os.path.join(os.path.dirname(__file__), "data", "pacientes.json")
    #Lẽ o arquivo e atribui os dados a variavel f, e depois retorna os dados em Json, em um formato de lista de dicionarios Python
    with open (caminho, "r", encoding="utf-8") as f:
        return json.load(f)
    
#Rota que traz o status da API
@app.route("/status")
def status():
    #Jsonfy permite eu trazer os dois valores juntos, o json e o código http
    return jsonify({
        "status": "success",
        "data": {
            "nome" : "Clinica Vet. API",
            "versao": "1.0.0",
            "status": "ok"
        }
    }), 200

# Rota que retorna todos os pacientes cadastrados
@app.route("/pacientes")
def listar_pacientes():
    try:
        pacientes = carregar_pacientes()
        return jsonify({
            "status" : "success",
            "total" : len(pacientes),
            "data": pacientes
        }),200
    #Exception capta erros e guarda na variavel e
    except Exception as e:
        return jsonify({
            "status" : "error",
            #Traz a mensagem de erro
            "mensagem" : str(e)
        }),500

# Rota que busca um unico paciente pelo id passado na URL
@app.route("/pacientes/<int:id>")
def buscar_pacientes(id):
    try:
        pacientes = carregar_pacientes()
        #Busca o paciente conforme  o filtro, caso não ter retorna none
        paciente = next((p for p in pacientes if p["id"] == id), None)

        #Resposta caso não tenha paciente com id do filtro
        if paciente is None:
            return jsonify({
                "status" : "error",
                "mensagem" : f"Paciente com o id {id} não foi encontrado"
            }), 404
        
        return jsonify({
            "status" : "success",
            "data" : paciente
        }), 200
    
    except Exception as e:
        return jsonify({
            "status" : "error",
            "mensagem": str(e)
        }),500


if __name__ == "__main__": # Só sobe o servidor se o arquivo for executado diretamente
    app.run(debug=True, host="0.0.0.0", port=5000) # debug=True reinicia ao salvar, host="0.0.0.0" permite acesso externo