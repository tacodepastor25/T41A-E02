-- Buscar proveedores cuyo nombre contiene 'Tech'
SELECT 
    rfc_proveedor,
    nombre_proveedor
FROM proveedor
WHERE LOWER(nombre_proveedor) LIKE '%tech%';
