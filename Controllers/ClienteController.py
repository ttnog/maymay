import mysql.connector
import models.Cliente as Cliente

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

def Incluir(cliente):
    try:
        conn = conexao()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Cliente (data, comeu, remedio, mood, fofoca, horario) VALUES (%s, %s, %s, %s, %s, %s)
        """, (cliente.data, cliente.comeu, cliente.remedio, cliente.mood, cliente.fofoca, cliente.horario))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def SelecionarTodos():
    try:
        conn = conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT data, comeu, remedio, mood, fofoca, horario FROM Cliente")
        clientes = []
        for linha in cursor.fetchall():
            clientes.append(Cliente.Cliente(*linha))
        return clientes
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()