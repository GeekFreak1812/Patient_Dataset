import pandas as pd
import random
import uuid
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Parameters
NUM_HOSPITALS = 5
NUM_PATIENTS = 100000
MIN_DIAGNOSES = 2
MIN_MEDICINES = 5

# 1. Hospital Table
hospital_data = []
for i in range(1, NUM_HOSPITALS + 1):
    hospital_data.append({
        'hospital_id': i,
        'hospital_name': f"{fake.company()} Hospital"
    })
hospital_df = pd.DataFrame(hospital_data)

# 2. Patient Table
patient_data = []
for i in range(1, NUM_PATIENTS + 1):
    hospital_id = random.randint(1, NUM_HOSPITALS)
    admission_date = fake.date_time_between(start_date='-2y', end_date='-1y')
    discharge_date = admission_date + timedelta(days=random.randint(1, 14))
    patient_data.append({
        'patient_id': i,
        'hospital_id': hospital_id,
        'patient_name': fake.name(),
        'dob': fake.date_of_birth(minimum_age=1, maximum_age=99),
        'admission_datetime': admission_date,
        'discharge_datetime': discharge_date
    })
patient_df = pd.DataFrame(patient_data)

# 3. Diagnosis Table
diagnosis_list = [
    'Hypertension', 'Diabetes', 'Asthma', 'COPD', 'Anemia',
    'Arthritis', 'Depression', 'Migraine', 'Heart Disease', 'Allergy'
]

diagnosis_data = []
diag_id_counter = 1
for patient in patient_df['patient_id']:
    num_diagnoses = random.randint(MIN_DIAGNOSES, MIN_DIAGNOSES + 2)
    diagnoses = random.sample(diagnosis_list, num_diagnoses)
    for diag in diagnoses:
        diagnosis_data.append({
            'diagnosis_id': diag_id_counter,
            'patient_id': patient,
            'diagnosis_name': diag
        })
        diag_id_counter += 1
diagnosis_df = pd.DataFrame(diagnosis_data)

# 4. Treatment Table
medicine_list = [
    'Paracetamol', 'Amoxicillin', 'Ibuprofen', 'Metformin', 'Atorvastatin',
    'Omeprazole', 'Amlodipine', 'Losartan', 'Albuterol', 'Gabapentin'
]

treatment_data = []
treat_id_counter = 1
for patient in patient_df['patient_id']:
    num_medicines = random.randint(MIN_MEDICINES, MIN_MEDICINES + 3)
    medicines = random.sample(medicine_list, num_medicines)
    for med in medicines:
        dose_time = random.choice(['Morning', 'Afternoon', 'Evening', 'Night'])
        duration_days = random.randint(3, 14)
        treatment_data.append({
            'treatment_id': treat_id_counter,
            'patient_id': patient,
            'medicine_name': med,
            'dose_time': dose_time,
            'duration': duration_days
        })
        treat_id_counter += 1
treatment_df = pd.DataFrame(treatment_data)

# 5. Billing Table
payment_modes = ['cash', 'credit']
billing_data = []
bill_id_counter = 1
for patient in patient_df['patient_id']:
    bill_amount = round(random.uniform(500, 5000), 2)
    payment_mode = random.choice(payment_modes)
    billing_data.append({
        'bill_id': bill_id_counter,
        'patient_id': patient,
        'bill_amount': bill_amount,
        'payment_mode': payment_mode
    })
    bill_id_counter += 1
billing_df = pd.DataFrame(billing_data)

# Example: Print shapes
print("Hospital Table:", hospital_df.shape)
print("Patient Table:", patient_df.shape)
print("Diagnosis Table:", diagnosis_df.shape)
print("Treatment Table:", treatment_df.shape)
print("Billing Table:", billing_df.shape)

# Optional: Save to CSV
hospital_df.to_csv("Hospital.csv", index=False)
patient_df.to_csv("Patient.csv", index=False)
diagnosis_df.to_csv("Diagnosis.csv", index=False)
treatment_df.to_csv("Treatment.csv", index=False)
billing_df.to_csv("Billing.csv", index=False)
