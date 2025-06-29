-- monthly income

SELECT
    strftime('%Y-%m', p.admission_datetime) AS year_month,
    b.payment_mode,
    SUM(b.bill_amount) AS total_income
FROM Billing b
JOIN Patient p
    ON b.patient_id = p.patient_id
GROUP BY year_month, b.payment_mode
ORDER BY year_month, b.payment_mode;

-- yearly income
SELECT
    strftime('%Y', p.admission_datetime) AS year,
    b.payment_mode,
    SUM(b.bill_amount) AS total_income
FROM Billing b
JOIN Patient p
    ON b.patient_id = p.patient_id
GROUP BY year, b.payment_mode
ORDER BY year, b.payment_mode;
