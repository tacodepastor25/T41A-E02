import psycopg2
import pytest

DB_PARAMS = {
    'dbname': 'test_db',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}


def get_connection():
    return psycopg2.connect(**DB_PARAMS)

def load_sql(filename):
    with open(filename, 'r') as f:
        return f.read()

def test_03_listar_todos_los_gastos():
    conn = get_connection()
    cur = conn.cursor()
    query = load_sql('03_listar_todos_los_gastos.sql')
    cur.execute(query)
    results = cur.fetchall()
    assert len(results) > 0
    cur.close()
    conn.close()

def test_04_total_gastado_por_cada_departamento():
    conn = get_connection()
    cur = conn.cursor()
    query = load_sql('04_total_gastado_por_cada_departamento.sql')
    cur.execute(query)
    results = cur.fetchall()
    assert all(row[1] >= 0 for row in results)
    cur.close()
    conn.close()

def test_05_total_de_gastos_por_dia():
    conn = get_connection()
    cur = conn.cursor()
    query = load_sql('05_total_de_gastos_por_dia.sql')
    cur.execute(query)
    results = cur.fetchall()
    assert all(row[2] >= 0 for row in results)
    cur.close()
    conn.close()

def test_06_buscar_proveedores_cuyo_nombre_contiene_tech():
    conn = get_connection()
    cur = conn.cursor()
    query = load_sql('06_buscar_proveedores_cuyo_nombre_contiene_tech.sql')
    cur.execute(query)
    results = cur.fetchall()
    assert all('tech' in row[1].lower() for row in results)
    cur.close()
    conn.close()

def test_07_mostrar_el_nombre_del_ususario_en_mayusculas():
    conn = get_connection()
    cur = conn.cursor()
    query = load_sql('07_mostrar_el_nombre_del_ususario_en_mayusculas.sql')
    cur.execute(query)
    results = cur.fetchall()
    assert all(row[0].isupper() for row in results)
    cur.close()
    conn.close()
