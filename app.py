import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

try:
    model = joblib.load("model.pkl")
except Exception:
    model = None

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None
    })

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "model not loaded"}), 503

    data = request.get_json()

    features = np.array([[
        data["sleep_hours"],
        data["heart_rate_resting"],
        data["hours_since_last_shift"],
        data["shift_length"]
    ]])

    score = model.predict_proba(features)[0][1] * 100

    return jsonify({"fatigue_score": round(float(score), 1)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)