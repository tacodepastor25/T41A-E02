-- Total gastado por cada departamento
SELECT d.nombre_departamento, SUM(g.monto) AS total_gastado
FROM gasto g JOIN departamento d ON g.id_departamento = d.id_departamento
GROUP BY d.nombre_departamento ORDER BY total_gastado DESC;
