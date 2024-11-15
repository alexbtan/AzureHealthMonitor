import logging
import json
import azure.functions as func
import matplotlib.pyplot as plt
from io import BytesIO

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    value = "Sent from Azure Functions"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "user@contoso.com"
            }]}],
        "subject": "Azure Functions email with SendGrid",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))

    return func.HttpResponse(f"Sent")

def create_visualization(data):
    """Generate a visualization using the health data."""
    # Extract data for visualization
    ages = [row[0] for row in data]
    cholesterol = [row[1] for row in data]
    max_heart_rate = [row[2] for row in data]
    blood_pressure = [row[3] for row in data]

    # Create a Matplotlib figure
    plt.figure(figsize=(10, 6))

    # Subplot 1: Age vs. Cholesterol
    plt.subplot(1, 2, 1)
    plt.scatter(ages, cholesterol, c='blue', alpha=0.6)
    plt.title("Age vs. Cholesterol")
    plt.xlabel("Age")
    plt.ylabel("Cholesterol (mg/dL)")

    # Subplot 2: Blood Pressure vs. Max Heart Rate
    plt.subplot(1, 2, 2)
    plt.scatter(blood_pressure, max_heart_rate, c='red', alpha=0.6)
    plt.title("Blood Pressure vs. Max Heart Rate")
    plt.xlabel("Resting Blood Pressure (mmHg)")
    plt.ylabel("Max Heart Rate (bpm)")

    plt.tight_layout()

    # Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer