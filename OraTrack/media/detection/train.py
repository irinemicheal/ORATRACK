import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ===============================
# 1️⃣ LOAD DATA
# ===============================
df = pd.read_csv("oral_cancer_clean.csv")

# ===============================
# 2️⃣ PREPROCESS CATEGORICAL DATA
# ===============================
# Convert Yes/No to 1/0
yes_no_cols = [
    "Tobacco Use", "Alcohol Consumption", "HPV Infection", "Betel Quid Use",
    "Chronic Sun Exposure", "Poor Oral Hygiene", "Family History of Cancer",
    "Compromised Immune System", "Oral Lesions", "Unexplained Bleeding",
    "Difficulty Swallowing", "White or Red Patches in Mouth"
]

for col in yes_no_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

# Map gender: Female=0, Male=1
df["Gender"] = df["Gender"].map({"Female": 0, "Male": 1})

# Map diet intake: Low=0, Moderate=1, High=2
df["Diet (Fruits & Vegetables Intake)"] = df["Diet (Fruits & Vegetables Intake)"].map({
    "Low": 0, "Moderate": 1, "High": 2
})

# ===============================
# 3️⃣ FEATURES & TARGET
# ===============================
X = df.drop(columns=["Cancer", "ID"])
y = df["Cancer"]

# ===============================
# 4️⃣ TRAIN / TEST SPLIT
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# ===============================
# 5️⃣ RANDOM FOREST MODEL
# ===============================
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=12,
    min_samples_split=10,
    min_samples_leaf=5,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

# ===============================
# 6️⃣ TRAIN
# ===============================
model.fit(X_train, y_train)

# ===============================
# 7️⃣ EVALUATE
# ===============================
y_pred = model.predict(X_test)

print("\n🎯 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# ===============================
# 8️⃣ FEATURE IMPORTANCE
# ===============================
importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n🔥 Feature Importance:\n", importance)

# ===============================
# 9️⃣ SAVE MODEL FOR DJANGO
# ===============================
joblib.dump(model, "oral_cancer_rf_model.pkl")
print("\n💾 Model saved successfully!")
