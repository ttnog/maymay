"""
import mysql.connector
from mysql.connector import Error

def delete_all_rows_and_reset_autoincrement(host, user, password, database, Clinte):
    try:
        #Estabelecendo a conexão com o banco de dados
        conn = mysql.connector.connect(
            host='roundhouse.proxy.rlwy.net',
            user='root',
            password='LnsTetyzLmcVRAPgxzIMWSqRejqNVmsy',
            database='railway',
            port=49703,
            auth_plugin='mysql_native_password',
        )
        
        if conn.is_connected():
            print("Conectado ao banco de dados")

            cursor = conn.cursor()

            #Excluir todas as linhas da tabela
            delete_query = f"DELETE FROM {Clinte}"
            cursor.execute(delete_query)
            print(f"Todas as linhas da tabela '{Clinte}' foram apagadas.")

            #Resetar o valor do auto-increment
            reset_autoincrement_query = f"ALTER TABLE {Clinte} AUTO_INCREMENT = 1"
            cursor.execute(reset_autoincrement_query)
            print(f"O valor do auto-increment da tabela '{Clinte}' foi resetado.")

            #Confirmar as mudanças
            conn.commit()

            cursor.close()
        else:
            print("Falha ao conectar ao banco de dados")

    except Error as e:
        print(f"Erro: {e}")

    finally:
        if conn.is_connected():
            conn.close()
            print("Conexão com o banco de dados encerrada")

#Parâmetros de conexão
host='roundhouse.proxy.rlwy.net',
user='root',
password='LnsTetyzLmcVRAPgxzIMWSqRejqNVmsy',
database='railway',
port=49703,
auth_plugin='mysql_native_password',
table = 'Cliente'

#Chamar a função para apagar as linhas e resetar o auto-increment
delete_all_rows_and_reset_autoincrement(host, user, password, database, table)
"""

import mysql.connector
from mysql.connector import Error

def delete_specific_rows_and_reset_autoincrement(host, user, password, database, table):
    try:
        # Estabelecendo a conexão com o banco de dados
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=49703,
            auth_plugin='mysql_native_password'
        )
        
        if conn.is_connected():
            print("Conectado ao banco de dados")

            cursor = conn.cursor()

            # Excluir apenas os IDs 9 e 10 da tabela
            delete_query = f"DELETE FROM {table} WHERE id IN (9, 10)"
            cursor.execute(delete_query)
            print(f"As linhas com IDs 9 e 10 da tabela '{table}' foram apagadas.")

            # Resetar o valor do auto-increment para começar a partir de 9
            reset_autoincrement_query = f"ALTER TABLE {table} AUTO_INCREMENT = 10"
            cursor.execute(reset_autoincrement_query)
            print(f"O valor do auto-increment da tabela '{table}' foi resetado para 10.")

            # Confirmar as mudanças
            conn.commit()

            cursor.close()
        else:
            print("Falha ao conectar ao banco de dados")

    except Error as e:
        print(f"Erro: {e}")

    finally:
        if conn.is_connected():
            conn.close()
            print("Conexão com o banco de dados encerrada")

# Parâmetros de conexão e tabela
host = 'roundhouse.proxy.rlwy.net'
user = 'root'
password = 'LnsTetyzLmcVRAPgxzIMWSqRejqNVmsy'
database = 'railway'
table = 'Cliente'

# Chamar a função para apagar os registros e resetar o auto-increment
delete_specific_rows_and_reset_autoincrement(host, user, password, database, table)