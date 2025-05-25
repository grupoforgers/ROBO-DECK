from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def run_web():
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import jsonify
from app.sensor_manager import obter_dados

@app.route("/api/sensores")
def sensores():
    return jsonify(obter_dados())
from flask import request
from app.motor_controller import enviar_comando

@app.route("/api/comando", methods=["POST"])
def comando():
    data = request.get_json()
    comando = data.get("acao")
    enviar_comando(comando)
    return jsonify({"status": "ok", "comando": comando})
