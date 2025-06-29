-- daily occupancy
SELECT
    hospital_id,
    DATE(admission_datetime) AS admission_date,
    COUNT(*) AS daily_admissions
FROM Patient
GROUP BY hospital_id, admission_date
ORDER BY hospital_id, admission_date;

--weekly occupancy
SELECT
    hospital_id,
    strftime('%Y-%W', admission_datetime) AS year_week,
    COUNT(*) AS weekly_admissions
FROM Patient
GROUP BY hospital_id, year_week
ORDER BY hospital_id, year_week;

-- monthly occupancy
SELECT
    hospital_id,
    strftime('%Y-%m', admission_datetime) AS year_month,
    COUNT(*) AS monthly_admissions
FROM Patient
GROUP BY hospital_id, year_month
ORDER BY hospital_id, year_month;

--yearly occupancy
SELECT
    hospital_id,
    strftime('%Y', admission_datetime) AS year,
    COUNT(*) AS yearly_admissions
FROM Patient
GROUP BY hospital_id, year
ORDER BY hospital_id, year;


