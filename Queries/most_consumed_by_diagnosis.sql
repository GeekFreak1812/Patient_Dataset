WITH MedicineUsage AS (
    SELECT
        d.diagnosis_name,
        t.medicine_name,
        COUNT(*) AS usage_count
    FROM Treatment t
    JOIN Diagnosis d
        ON t.patient_id = d.patient_id
    GROUP BY d.diagnosis_name, t.medicine_name
)
SELECT
    diagnosis_name,
    medicine_name,
    usage_count
FROM (
    SELECT
        diagnosis_name,
        medicine_name,
        usage_count,
        RANK() OVER (PARTITION BY diagnosis_name ORDER BY usage_count DESC) AS rnk
    FROM MedicineUsage
)
WHERE rnk = 1;

-- Join Treatment and Diagnosis via patient_id.

-- Group by diagnosis_name and medicine_name.
-- WITH computes usage counts.

-- RANK() assigns ranks per diagnosis.

-- WHERE rnk=1 picks the top medicine per diagnosis.
