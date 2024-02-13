-- adds 2 col
-- and orders by desc fan count
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
