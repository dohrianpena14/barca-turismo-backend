import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.database.connection import get_connection

def obtener_ofertas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ofertas_turisticas WHERE activa = TRUE")
    ofertas = cursor.fetchall()

    cursor.close()
    conn.close()

    return ofertas