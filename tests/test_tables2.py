import psycopg2
import pytest

# Parámetros de conexión
DB_PARAMS = {
    'dbname': 'test_db',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Función para obtener conexión
def get_connection():
    return psycopg2.connect(**DB_PARAMS)

def test_usuario_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='usuario';")
    columns = [row[0] for row in cur.fetchall()]
    expected_columns = {'id_usuario', 'nombre_usuario'}
    assert expected_columns.issubset(set(columns))
    cur.close()
    conn.close()

def test_departamento_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='departamento';")
    columns = [row[0] for row in cur.fetchall()]
    expected_columns = {'id_departamento', 'nombre_departamento'}
    assert expected_columns.issubset(set(columns))
    cur.close()
    conn.close()

def test_cuenta_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='cuenta';")
    columns = [row[0] for row in cur.fetchall()]
    expected_columns = {'id_cuenta', 'nombre_cuenta'}
    assert expected_columns.issubset(set(columns))
    cur.close()
    conn.close()

def test_tipo_de_gasto_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='tipo_de_gasto';")
    columns = [row[0] for row in cur.fetchall()]
    expected_columns = {'id_tipo_gasto', 'nombre_tipo_gasto', 'id_cuenta'}
    assert expected_columns.issubset(set(columns))
    cur.close()
    conn.close()

def test_proveedor_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='proveedor';")
    columns = [row[0] for row in cur.fetchall()]
    expected_columns = {'rfc_proveedor', 'nombre_proveedor'}
    assert expected_columns.issubset(set(columns))
    cur.close()
    conn.close()

def test_gasto_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='gasto';")
    columns = [row[0] for row in cur.fetchall()]
    expected_columns = {'id_gasto', 'id_usuario', 'id_tipo_gasto', 'id_departamento', 'rfc_proveedor', 'monto', 'fecha'}
    assert expected_columns.issubset(set(columns))
    cur.close()
    conn.close()


def get_connection():
    return psycopg2.connect(**DB_PARAMS)

def get_foreign_keys(table_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            kcu.column_name,
            ccu.table_name AS foreign_table_name,
            ccu.column_name AS foreign_column_name
        FROM
            information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
              ON tc.constraint_name = kcu.constraint_name
              AND tc.table_schema = kcu.table_schema
            JOIN information_schema.constraint_column_usage AS ccu
              ON ccu.constraint_name = tc.constraint_name
              AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s;
    """, (table_name,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def test_foreign_keys_tipo_de_gasto():
    fks = get_foreign_keys('tipo_de_gasto')
    assert ('id_cuenta', 'cuenta', 'id_cuenta') in fks

def test_foreign_keys_gasto():
    fks = get_foreign_keys('gasto')
    expected_fks = [
        ('id_usuario', 'usuario', 'id_usuario'),
        ('id_tipo_gasto', 'tipo_de_gasto', 'id_tipo_gasto'),
        ('id_departamento', 'departamento', 'id_departamento'),
        ('rfc_proveedor', 'proveedor', 'rfc_proveedor')
    ]
    for fk in expected_fks:
        assert fk in fks
