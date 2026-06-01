import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.database.connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM reservas")

reservas = cursor.fetchall()

for reserva in reservas:
    print(reserva)

cursor.close()
conn.close()