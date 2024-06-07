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
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Cliente (data, comeu, mood, fofoca) VALUES (%s, %s, %s, %s)
    """, (cliente.data, cliente.comeu, cliente.mood, cliente.fofoca))
    conn.commit()
    conn.close()

def SelecionarTodos():
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT data, comeu, mood, fofoca FROM Cliente")
    clientes = []
    for linha in cursor.fetchall():
        clientes.append(Cliente.Cliente(*linha))
    conn.close()
    return clientes