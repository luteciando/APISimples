from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "feito": False},
    {"id": 2, "titulo": "Criar API Flask", "feito": True}
]

@app.route("/")
def home():
    return jsonify({"mensagem": "Bem-vindo à minha API Flask!"})

@app.route("/tarefas", methods=["GET"])
def get_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def add_tarefa():
    nova_tarefa = request.get_json()
    nova_tarefa["id"] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

if __name__ == "__main__":
    app.run(debug=True)
