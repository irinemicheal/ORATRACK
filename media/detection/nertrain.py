# ======================================
# 1️⃣ IMPORT LIBRARIES
# ======================================
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from xgboost import XGBClassifier

# ======================================
# 2️⃣ LOAD DATA
# ======================================
df = pd.read_csv("oral_cancer.csv")
print("Dataset Shape:", df.shape)

# ======================================
# 3️⃣ DROP ID COLUMN
# ======================================
df = df.drop(columns=["ID"])

# ======================================
# 4️⃣ ENCODE CATEGORICAL VARIABLES
# ======================================

# Yes/No columns
yes_no_columns = [
    "Tobacco Use", "Alcohol Consumption", "HPV Infection",
    "Betel Quid Use", "Chronic Sun Exposure", "Poor Oral Hygiene",
    "Family History of Cancer", "Compromised Immune System",
    "Oral Lesions", "Unexplained Bleeding", "Difficulty Swallowing",
    "White or Red Patches in Mouth", "Oral Cancer (Diagnosis)"
]

for col in yes_no_columns:
    df[col] = df[col].map({"Yes": 1, "No": 0})

# Gender
df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})

# Diet
df["Diet (Fruits & Vegetables Intake)"] = df["Diet (Fruits & Vegetables Intake)"].map({
    "Low": 0, "Moderate": 1, "High": 2
})

# ======================================
# 5️⃣ FEATURE ENGINEERING
# ======================================

# Risk score based on main risk factors
df["Risk_Score"] = (
    df["Tobacco Use"] * 2 +
    df["Alcohol Consumption"] * 1 +
    df["HPV Infection"] * 2 +
    df["Oral Lesions"] * 3 +
    df["White or Red Patches in Mouth"] * 3 +
    df["Difficulty Swallowing"] * 2 +
    df["Unexplained Bleeding"] * 2
)

# Interaction features
df["Tobacco_Alcohol"] = df["Tobacco Use"] * df["Alcohol Consumption"]
df["Lesion_Patches"] = df["Oral Lesions"] * df["White or Red Patches in Mouth"]

# ======================================
# 6️⃣ FEATURES & TARGET
# ======================================
X = df.drop(columns=["Oral Cancer (Diagnosis)"])
y = df["Oral Cancer (Diagnosis)"]

# ======================================
# 7️⃣ TRAIN / TEST SPLIT
# ======================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# ======================================
# 8️⃣ SCALING
# ======================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ======================================
# 9️⃣ TRAIN XGBOOST MODEL
# ======================================
model = XGBClassifier(
    n_estimators=500,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train_scaled, y_train)

# ======================================
# 🔟 EVALUATE
# ======================================
y_pred = model.predict(X_test_scaled)

print("\n🎯 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))
print("\n📌 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# ======================================
# 1️⃣1️⃣ FEATURE IMPORTANCE
# ======================================
importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n🔥 Feature Importance:\n")
print(importance)

# ======================================
# 1️⃣2️⃣ SAVE MODEL & SCALER
# ======================================
joblib.dump(model, "oral_cancer_model_new.pkl")
joblib.dump(scaler, "scaler.pkl")
print("\n💾 Model & Scaler Saved Successfully!")
