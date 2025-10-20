INSERT INTO usuario (id_usuario, nombre_usuario) VALUES
(1, 'José Méndez'),
(2, 'Ana Torres'),
(3, 'Luis Martínez'),
(4, 'Carla Gómez'),
(5, 'Miguel Sánchez');

INSERT INTO departamento (id_departamento, nombre_departamento) VALUES
(1, 'Finanzas'),
(2, 'Recursos Humanos'),
(3, 'TI'),
(4, 'Marketing'),
(5, 'Operaciones');

INSERT INTO cuenta (id_cuenta, nombre_cuenta) VALUES
(1, 'Cuenta General'),
(2, 'Cuenta RH'),
(3, 'Cuenta TI'),
(4, 'Cuenta Marketing'),
(5, 'Cuenta Operativa');

INSERT INTO tipo_de_gasto (id_tipo_gasto, nombre_tipo_gasto, id_cuenta) VALUES
(1, 'Papelería', 1),
(2, 'Capacitación', 2),
(3, 'Software', 3),
(4, 'Publicidad', 4),
(5, 'Mantenimiento', 5);

INSERT INTO proveedor (rfc_proveedor, nombre_proveedor) VALUES
('XAXX010101000', 'Papelería Central'),
('BEBE020202111', 'Cursos RH'),
('TECH030303222', 'SoftTech'),
('MARK040404333', 'Publicidad MX'),
('FIX050505444', 'Servicios Técnicos');

INSERT INTO gasto (id_gasto, id_usuario, id_tipo_gasto, id_departamento, rfc_proveedor, monto, fecha) VALUES
(1, 1, 1, 1, 'XAXX010101000', 1500.00, '2025-10-01'),
(2, 2, 2, 2, 'BEBE020202111', 3200.00, '2025-10-02'),
(3, 3, 3, 3, 'TECH030303222', 5000.00, '2025-10-03'),
(4, 4, 4, 4, 'MARK040404333', 4200.00, '2025-10-04'),
(5, 5, 5, 5, 'FIX050505444', 2800.00, '2025-10-05');
``

