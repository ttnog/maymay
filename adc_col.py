import mysql.connector
from mysql.connector import Error

def conexao():
    conn = mysql.connector.connect(
        host='roundhouse.proxy.rlwy.net',
        user='root',
        password='LnsTetyzLmcVRAPgxzIMWSqRejqNVmsy',
        database='railway',
        port=49703,
        auth_plugin='mysql_native_password'
    )
    return conn

def adicionar_colunas():
    try:
        conn = conexao()
        cursor = conn.cursor()

        # Lista de colunas a serem adicionadas
        colunas = {
            'data': 'DATE NOT NULL',
            'horario': 'TIME',
            'comeu': 'VARCHAR(10) NOT NULL',
            'mood': 'INT NOT NULL',
            'fofoca': 'TEXT',
            'remedio': 'VARCHAR(10) NOT NULL',
        }

        # Verificar e adicionar cada coluna, se necessário
        for coluna, tipo in colunas.items():
            cursor.execute(f"SHOW COLUMNS FROM Cliente LIKE '{coluna}'")
            resultado = cursor.fetchone()
            if not resultado:
                cursor.execute(f"ALTER TABLE Cliente ADD COLUMN {coluna} {tipo}")
                print(f"Coluna '{coluna}' adicionada.")

        conn.commit()
    except Error as err:
        print(f"Erro: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Chamar a função para adicionar as colunas
adicionar_colunas()