SELECT
    medicine_name,
    COUNT(*) AS times_used
FROM Treatment
GROUP BY medicine_name
ORDER BY times_used DESC
LIMIT 1;
