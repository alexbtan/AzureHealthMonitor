import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# Step 1: Load the CSV Data
data = pd.read_csv('heart.csv')  # Replace 'health_data.csv' with your actual file path

# Step 2: Inspect Data (Optional)
print(data.head())
print(data.info())

# Step 3: Preprocess the Data
# Assuming the target column is named 'heart_disease' where 1 = disease, 0 = no disease
# Replace 'heart_disease' with the actual name of the target column if different
target_column = 'target'
X = data.drop(columns=[target_column])  # Features
y = data[target_column]  # Target

# Optional: Convert categorical columns if needed
# X = pd.get_dummies(X)  # Uncomment if your data has categorical features

# Step 4: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a Model
# Using RandomForestClassifier for binary classification
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Make Predictions and Evaluate
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 7: Save the Model for Later Use
dump(model, 'heart_disease_model.pkl')
print("Model saved as heart_disease_model.pkl")
