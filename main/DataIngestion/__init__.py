import json
import azure.functions as func
from datetime import datetime
import random

def simulate_health_data():
    """Simulate health data for a patient."""
    return {
        "age": random.randint(29, 100),                 # Age in realistic range
        "sex": random.choice([0, 1]),                  # 0 = Female, 1 = Male
        "cp": random.randint(0, 3),                    # Chest pain type (0-3)
        "trestbps": random.randint(90, 200),           # Resting blood pressure
        "chol": random.randint(126, 564),              # Serum cholesterol in mg/dl
        "fbs": random.choice([0, 1]),                  # Fasting blood sugar > 120 mg/dl
        "restecg": random.randint(0, 2),               # Resting electrocardiographic results (0-2)
        "thalach": random.randint(71, 202),            # Maximum heart rate achieved
        "exang": random.choice([0, 1]),                # Exercise-induced angina (0 = No, 1 = Yes)
        "oldpeak": round(random.uniform(0.0, 6.2), 1), # ST depression induced by exercise
        "slope": random.randint(0, 2),                 # Slope of peak exercise ST segment
        "ca": random.randint(0, 3),                    # Number of major vessels (0-3)
        "thal": random.randint(0, 3)                   # Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
    }

def validate_data(data):
    """Validate that all fields in health data are present and contain valid values."""
    # Required fields and their acceptable ranges or types
    required_fields = {
        "age": lambda x: isinstance(x, int) and 29 <= x <= 120,
        "sex": lambda x: x in [0, 1],
        "cp": lambda x: 0 <= x <= 3,
        "trestbps": lambda x: isinstance(x, int) and 90 <= x <= 200,
        "chol": lambda x: isinstance(x, int) and 126 <= x <= 564,
        "fbs": lambda x: x in [0, 1],
        "restecg": lambda x: 0 <= x <= 2,
        "thalach": lambda x: isinstance(x, int) and 71 <= x <= 202,
        "exang": lambda x: x in [0, 1],
        "oldpeak": lambda x: isinstance(x, float) and 0.0 <= x <= 6.2,
        "slope": lambda x: 0 <= x <= 2,
        "ca": lambda x: 0 <= x <= 3,
        "thal": lambda x: 0 <= x <= 3
    }

    # Validate each field
    for field, condition in required_fields.items():
        if field not in data or not condition(data[field]):
            return False  # Return False if any field is missing or invalid
    return True

def main(newPatientAdded, HealthMetrics: func.Out[func.SqlRow]):
    print("New Patient Added to System")
    newPatientData = simulate_health_data()
    if validate_data(newPatientData):
        # Data is valid; proceed to insert
        row = func.SqlRow(newPatientData)
        HealthMetrics.set(row)
        print("Patient data successfully added to HealthMetrics table")
    else:
        print("Invalid Data encountered for patient")