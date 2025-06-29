--strftime('%Y-%m', date) Extracts Year-Month.

--strftime('%Y-%W', date) Extracts Year-Week.

--strftime('%Y', date)Extracts Year.





SELECT
    hospital_id,
    AVG(patient_count) AS avg_patients_per_month
FROM (
    SELECT
        hospital_id,
        strftime('%Y-%m', admission_datetime) AS year_month,
        COUNT(*) AS patient_count
    FROM Patient
    GROUP BY hospital_id, year_month
)
GROUP BY hospital_id;


-- Average patients per week
SELECT
    hospital_id,
    AVG(patient_count) AS avg_patients_per_week
FROM (
    SELECT
        hospital_id,
        strftime('%Y-%W', admission_datetime) AS year_week,
        COUNT(*) AS patient_count
    FROM Patient
    GROUP BY hospital_id, year_week
)
GROUP BY hospital_id;

-- Average patients per year
SELECT
    hospital_id,
    AVG(patient_count) AS avg_patients_per_year
FROM (
    SELECT
        hospital_id,
        strftime('%Y', admission_datetime) AS year,
        COUNT(*) AS patient_count
    FROM Patient
    GROUP BY hospital_id, year
)
GROUP BY hospital_id;

