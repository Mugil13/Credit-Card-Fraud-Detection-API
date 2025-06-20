from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load model and preprocessors
model = joblib.load("models/voting_model.pkl")
pca = joblib.load("models/pca.pkl")
scaler = joblib.load("models/scaler.pkl")

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "API running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data["features"]).reshape(1, -1)

        # Scale the last two columns (Time, Amount)
        features[:, -2:] = scaler.transform(features[:, -2:])

        # Apply PCA
        features_pca = pca.transform(features)

        # Predict
        prediction = model.predict(features_pca)[0]
        probability = model.predict_proba(features_pca)[0][1]

        return jsonify({
            "fraud_prediction": int(prediction),
            "fraud_probability": round(float(probability), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
