import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database (this creates a file 'mydatabase.db')
engine = create_engine('sqlite:///mydatabase.db')

# Read CSVs
hospital_df = pd.read_csv("Hospital.csv")
patient_df = pd.read_csv("Patient.csv")
diagnosis_df = pd.read_csv("Diagnosis.csv")
treatment_df = pd.read_csv("Treatment.csv")
billing_df = pd.read_csv("Billing.csv")

# Write tables to SQLite
hospital_df.to_sql("Hospital", engine, if_exists="replace", index=False)
patient_df.to_sql("Patient", engine, if_exists="replace", index=False)
diagnosis_df.to_sql("Diagnosis", engine, if_exists="replace", index=False)
treatment_df.to_sql("Treatment", engine, if_exists="replace", index=False)
billing_df.to_sql("Billing", engine, if_exists="replace", index=False)

print("✅ All tables loaded into SQLite database 'mydatabase.db'")
