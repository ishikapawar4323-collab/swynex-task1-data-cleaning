import pandas as pd

# Load dataset
df = pd.read_csv("Titanic_Raw.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Standardize text
df["Sex"] = df["Sex"].str.strip().str.lower()
df["Embarked"] = df["Embarked"].str.strip().str.upper()

# Save cleaned dataset
df.to_csv("Titanic_Cleaned.csv", index=False)

print("Cleaning completed successfully!")