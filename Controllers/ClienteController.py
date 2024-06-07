import services.database as db
import models.Cliente as cliente

def Incluir(cliente):
    db.cursor.execute("""
        INSERT INTO Cliente(cliData, cliComeu, cliMood, cliFofoca) 
        VALUES (?, ?, ?, ?)""", (cliente.data, cliente.comeu, cliente.mood, cliente.fofoca))
    db.con.commit()

def SelecionarTodos():
    db.cursor.execute('SELECT * FROM Cliente')
    customerList = []

    for row in db.cursor.fetchall():
        customerList.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4]))
    return customerList