from flask import Flask, request, jsonify
from quantum_optimizer import quantum_route_optimizer

app = Flask(__name__)

# 1️⃣ Root endpoint
@app.route("/")
def home():
    return "Hello DevOps Intern!"

# 2️⃣ Health check endpoint
@app.route("/health")
def health():
    return "OK"

# 3️⃣ Existing quantum optimization endpoint
@app.route("/optimize-route", methods=["POST"])
def optimize_route():
    data = request.get_json()
    zones = data.get("zones")

    optimized_route = quantum_route_optimizer(zones)

    return jsonify({
        "status": "success",
        "optimized_route": optimized_route
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
