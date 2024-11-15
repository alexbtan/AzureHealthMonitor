import azure.functions as func
import json
import joblib
from datetime import datetime

# Load the heart disease prediction model
MODEL_PATH = 'heart_disease_model.pkl'
model = joblib.load(MODEL_PATH)

def predict_heart_disease(patient_data):
    """Predict heart disease risk based on patient data using the ML model."""
    features = [[
        patient_data["age"],
        patient_data["sex"],
        patient_data["cp"],
        patient_data["trestbps"],
        patient_data["chol"],
        patient_data["fbs"],
        patient_data["restecg"],
        patient_data["thalach"],
        patient_data["exang"],
        patient_data["oldpeak"],
        patient_data["slope"],
        patient_data["ca"],
        patient_data["thal"]
    ]]
    heart_disease_risk = model.predict(features)[0]
    return "high risk" if heart_disease_risk == 1 else "low risk"

def main(newPatientTrigger, patient: func.Out[func.SqlRow], employees: func.SqlRowList):
    rows = list(map(lambda r: json.loads(r.to_json()), employees))
    patient_data = rows[-1]
    print(patient_data)

    heart_disease_risk = predict_heart_disease(patient_data)
    print(f"Predicted heart disease risk for patient {patient_data['patient_id']}: {heart_disease_risk}")
    risk_data = {
        "patient_id" : patient_data["patient_id"],
        "risk_level" : heart_disease_risk,
        "prediction_timestamp" : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    row = func.SqlRow(risk_data)
    patient.set(row)