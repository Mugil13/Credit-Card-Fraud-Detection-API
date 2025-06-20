# Credit Card Fraud Detection – End-to-End ML Pipeline with API Tool

This is a full-stack ML project to detect fraudulent credit card transactions using real-time anonymized data. I have implemented preprocessing, model building (contains some ensemble approaches too), API deployment with Flask & Docker, and finally monitoring everything with Prometheus + Grafana.

---

## Tech Stack Used

- **ML Models**: Logistic Regression, Random Forest, XGBoost, Voting & Stacking Classifiers
- **Preprocessing**: PCA, SMOTE
- **API Deployment**: Flask + Docker
- **Monitoring APIs**: Prometheus + Grafana

---

## Model Performance

| Model            | Precision | Recall | F1 Score | AUC   |
|------------------|-----------|--------|----------|-------|
| Logistic         | 0.05      | 0.91   | 0.10     | 0.97  |
| Random Forest    | 0.83      | 0.83   | 0.83     | 0.95  |
| XGBoost          | 0.61      | 0.86   | 0.71     | 0.97  |
| Voting Classifier| 0.68      | 0.88   | 0.77     | 0.97  |
| Stacking         | 0.79      | 0.84   | 0.81     | 0.94  |

```
I have also included Overfitting Check and ROC curve plotting for better understanding
```

---

## Setup

Run the following command

```
docker-compose up --build
```

Then open:

- Flask API: http://localhost:5000

- Prometheus: http://localhost:9090

- Grafana: http://localhost:3000

Login to Grafana: admin / admin
Add Prometheus data source at http://host.docker.internal:9090

## Test the API

Use this curl command or you can also use Postman and ThunderClient:

```
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"features\": [-2.31, 1.95, -1.60, 3.99, -0.52, -1.42, -2.53, 1.39, -2.77, -2.77, 3.20, -2.89, -0.59, -4.28, 0.38, -1.14, -2.83, -0.01, 0.41, 0.12, 0.51, -0.03, -0.46, 0.32, 0.04, 0.17, 0.26, -0.14, 0, 406]}"
```

Sample Response:

json
{
  "fraud_prediction": 1,
  "fraud_probability": 0.99
}


## Key Features

- PCA to reduce dimensionality

- SMOTE to handle class imbalance

- 5 ML models with F1/AUC tracking

- Voting classifier deployed as API

- Real-time metrics via Prometheus + Grafana

- Fully containerized

## License

This project is under MIT License