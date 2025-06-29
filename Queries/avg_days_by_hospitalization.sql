SELECT
    AVG(julianday(discharge_datetime) - julianday(admission_datetime)) AS avg_days_hospitalized
FROM Patient;

-- julianday(discharge) - julianday(admission) computes length of stay in days.
