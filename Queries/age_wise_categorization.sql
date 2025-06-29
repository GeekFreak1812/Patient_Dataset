SELECT
    CASE
        WHEN CAST((julianday('now') - julianday(dob))/365.25 AS INTEGER) < 18 THEN 'Child'
        WHEN CAST((julianday('now') - julianday(dob))/365.25 AS INTEGER) BETWEEN 18 AND 64 THEN 'Adult'
        ELSE 'Senior'
    END AS age_category,
    COUNT(*) AS patient_count
FROM Patient
GROUP BY age_category;
