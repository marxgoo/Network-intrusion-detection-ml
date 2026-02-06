import joblib
import json
import numpy as np
from alert_generator import generate_alert

MODEL_PATH = r"C:\Users\dell\OneDrive\Bureau\NIDS\models\random_forest_model.pkl"
SCALER_PATH = r"C:\Users\dell\OneDrive\Bureau\NIDS\models\scaler.pkl"
FEATURES_PATH = r"C:\Users\dell\OneDrive\Bureau\NIDS\features.json"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

with open(FEATURES_PATH, "r") as f:
    selected_features = json.load(f)

def predict_flow(flow_features):
    try:
        X = np.array([[flow_features[f] for f in selected_features]])
        X_scaled = scaler.transform(X)
        pred = model.predict(X_scaled)[0]

        if pred == 1:
            print(f"Anomalie détectée: {flow_features['Src IP']} → {flow_features['Dst IP']}")
            generate_alert(flow_features)

    except Exception as e:
        print("ERROR Predictor", e)
