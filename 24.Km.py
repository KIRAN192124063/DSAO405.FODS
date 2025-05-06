import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

data = {
    "Symptom1": [1.2, 2.3, 3.1, 0.5, 1.8],
    "Symptom2": [3.5, 1.2, 0.8, 2.9, 3.1],
    "Condition": [0, 1, 0, 1, 0]  
}

df = pd.DataFrame(data)


X = df.drop(columns=["Condition"])
y = df["Condition"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

new_patient_features = []
num_features = X.shape[1]
print(f"Enter {num_features} symptom values for the new patient:")
for i in range(num_features):
    value = float(input(f"Symptom {i+1}: "))
    new_patient_features.append(value)
X = df.drop(columns=["Condition"])
y = df["Condition"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

new_patient_features = []
num_features = X.shape[1]
print(f"Enter {num_features} symptom values for the new patient:")
for i in range(num_features):
    value = float(input(f"Symptom {i+1}: "))
    new_patient_features.append(value)

k = int(input("Enter the value of k (number of neighbors): "))

knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
new_patient_scaled = scaler.transform([new_patient_features])

prediction = knn.predict(new_patient_scaled)
condition_status = "Has the medical condition" if prediction[0] == 1 else "Does not have the medical condition"

print(f"Prediction: {condition_status}")
