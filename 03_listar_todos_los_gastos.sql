-- Listar todos los gastos con información del usuario, tipo de gasto y proveedor
SELECT g.id_gasto, u.nombre_usuario, tg.nombre_tipo_gasto, p.nombre_proveedor, g.monto, g.fecha
FROM gasto g JOIN usuario u ON g.id_usuario = u.id_usuario
JOIN tipo_de_gasto tg ON g.id_tipo_gasto = tg.id_tipo_gasto
JOIN proveedor p ON g.rfc_proveedor = p.rfc_proveedor;
