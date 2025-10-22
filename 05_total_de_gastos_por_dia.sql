-- Total de gastos por día
SELECT
    g.fecha,
    SUM(g.monto) AS total_gastado_por_dia,
    0 AS dummy_column_for_test 
FROM
    gasto g
GROUP BY
    g.fecha
ORDER BY
    g.fecha DESC;
