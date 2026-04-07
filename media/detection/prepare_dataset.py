import pandas as pd

# ===============================
# 1️⃣ LOAD DATA
# ===============================
df = pd.read_csv("oral_cancer.csv")

# Strip accidental spaces in column names
df.columns = df.columns.str.strip()

print("📌 Columns found:\n", df.columns.tolist())

# ===============================
# 2️⃣ ENCODING MAPS
# ===============================
yes_no_map = {"Yes": 1, "No": 0}
gender_map = {"Male": 1, "Female": 0}
diet_map = {"Low": 0, "Moderate": 1, "High": 2}

# ===============================
# 3️⃣ APPLY ENCODING
# ===============================

# Gender
df["Gender"] = df["Gender"].map(gender_map)

# Diet column (FULL NAME)
df["Diet (Fruits & Vegetables Intake)"] = df[
    "Diet (Fruits & Vegetables Intake)"
].map(diet_map)

# Binary columns (FULL NAMES)
binary_columns = [
    "Tobacco Use",
    "Alcohol Consumption",
    "HPV Infection",
    "Betel Quid Use",
    "Chronic Sun Exposure",
    "Poor Oral Hygiene",
    "Family History of Cancer",
    "Compromised Immune System",
    "Oral Lesions",
    "Unexplained Bleeding",
    "Difficulty Swallowing",
    "White or Red Patches in Mouth",
    "Oral Cancer (Diagnosis)"
]

for col in binary_columns:
    if col not in df.columns:
        raise ValueError(f"❌ Column missing: {col}")
    df[col] = df[col].map(yes_no_map)

# ===============================
# 4️⃣ RENAME TARGET COLUMN
# ===============================
df.rename(columns={
    "Oral Cancer (Diagnosis)": "Cancer"
}, inplace=True)

# ===============================
# 5️⃣ CHECK FOR NaNs
# ===============================
if df.isnull().sum().any():
    print("⚠️ NaN values found:")
    print(df.isnull().sum())
    raise ValueError("Fix encoding values in CSV (case mismatch?)")

# ===============================
# 6️⃣ SAVE CLEAN DATASET
# ===============================
df.to_csv("oral_cancer_clean.csv", index=False)

print("\n✅ Dataset prepared successfully!")
print(df.head())
