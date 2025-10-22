# T41A-E02

## NORMALIZACIÓN
Identifique las entidades y las relaciones del siguiente requerimiento de registro de información.   

Después normaliza las tablas hasta la tercera **forma normal (3FN)**.   

"La aplicación `gastos` registrará el `usuario` el `tipo_de_gasto`, esto se relaciona con la `cuenta`  
asociada al `tipo_de_gasto`, también se registrará el `departamento` en la segunda pantalla   
se tiene una forma con el `monto`, el `RFC` del proveedor y el `nombre_del_proveedor` "

Toma como referencia los siguientes nombres de tablas y/o columnas y    
agrega las **llaves foráneas** donde corresponda.

- `usuario`   
- `id_usuario`   
- `nombre_usuario`   
- `departamento`
- `id_departamento`
- `nombre_departamento`
- `cuenta`
- `id_cuenta`
- `nombre_cuenta`
- `tipo_de_gasto`
- `id_tipo_gasto`
- `nombre_tipo_gasto`
- `id_cuenta`
- `rfc_proveedor`
- `nombre_proveedor`
- `gasto`
- `id_gasto`
- `id_usuario`
- `id_tipo_gasto`
- `id_departamento`
- `rfc_proveedor`
- `monto`
- `fecha`

## CONSULTAS
Después de generar los DDLs delas tablas normailizadas ingresa las consultas descritas en los archivos 03 al 07
