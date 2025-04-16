
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/get-rodadas")
def get_rodadas():
    # Simulação de scraping com rodadas fictícias (ex: multiplicadores)
    rodadas = [round(random.uniform(1.0, 10.0), 2) for _ in range(15)]
    return jsonify(rodadas)

@app.route("/prever")
def prever():
    # Simula uma previsão inteligente com chance acima de 90%
    padrao_detectado = random.choice([True, False])
    if padrao_detectado:
        chance = round(random.uniform(94.0, 99.5), 2)
        mensagem = "Alerta: Alta probabilidade de rodada rosa!"
    else:
        chance = round(random.uniform(80.0, 93.5), 2)
        mensagem = "Risco moderado. Padrões instáveis."

    return jsonify({
        "mensagem": mensagem,
        "chance": chance
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
