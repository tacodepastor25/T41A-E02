CREATE TABLE departamento (
    id_departamento SERIAL PRIMARY KEY,
    nombre_departamento VARCHAR(100) NOT NULL UNIQUE
);

-- USUARIO
CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL UNIQUE
);

-- CUENTA
CREATE TABLE cuenta (
    id_cuenta SERIAL PRIMARY KEY,
    nombre_cuenta VARCHAR(100) NOT NULL UNIQUE
);

-- TIPO GATSO
CREATE TABLE tipo_de_gasto (
    id_tipo_gasto SERIAL PRIMARY KEY,
    nombre_tipo_gasto VARCHAR(100) NOT NULL UNIQUE,
    id_cuenta INTEGER NOT NULL,
    CONSTRAINT fk_cuenta
        FOREIGN KEY (id_cuenta)
        REFERENCES cuenta(id_cuenta)
);

-- PROOVEDOR
CREATE TABLE proveedor (
    rfc_proveedor VARCHAR(13) PRIMARY KEY, -- RFC como clave primaria
    nombre_proveedor VARCHAR(255) NOT NULL
);

-- GASTO
CREATE TABLE gasto (
    id_gasto SERIAL PRIMARY KEY,
    monto NUMERIC(10, 2) NOT NULL CHECK (monto >= 0),
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    id_usuario INTEGER NOT NULL,
    id_tipo_gasto INTEGER NOT NULL,
    id_departamento INTEGER NOT NULL,
    rfc_proveedor VARCHAR(13) NOT NULL,
    
    CONSTRAINT fk_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario),
    
    CONSTRAINT fk_tipo_gasto
        FOREIGN KEY (id_tipo_gasto)
        REFERENCES tipo_de_gasto(id_tipo_gasto),
        
    CONSTRAINT fk_departamento
        FOREIGN KEY (id_departamento)
        REFERENCES departamento(id_departamento),
        
    CONSTRAINT fk_proveedor
        FOREIGN KEY (rfc_proveedor)
        REFERENCES proveedor(rfc_proveedor)
);
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_tipo_gasto) REFERENCES tipo_de_gasto(id_tipo_gasto),
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento),
    FOREIGN KEY (rfc_proveedor) REFERENCES proveedor(rfc_proveedor)
);
