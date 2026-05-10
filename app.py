from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    features = np.array([[
        data["sleep_hours"],
        data["heart_rate_resting"],
        data["hours_since_last_shift"],
        data["shift_length"]
    ]])
    
    score = model.predict_proba(features)[0][1] * 100

    return jsonify({"fatigue_score": round(float(score), 1)})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()