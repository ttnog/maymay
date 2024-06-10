import mysql.connector

conn = mysql.connector.connect(
    host='roundhouse.proxy.rlwy.net',
    user='root',
    password='LnsTetyzLmcVRAPgxzIMWSqRejqNVmsy',
    database='railway',
    port=49703,
    auth_plugin='mysql_native_password',
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    horario TIME,          
    comeu VARCHAR(10) NOT NULL,
    mood INT NOT NULL,
    fofoca TEXT
)
""")

conn.commit()
conn.close()