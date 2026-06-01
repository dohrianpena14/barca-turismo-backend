import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.database.connection import get_connection

def obtener_ofertas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, descripcion, ciudad, precio, imagen_url, activa
        FROM ofertas_turisticas
        WHERE activa = TRUE
    """)

    filas = cursor.fetchall()

    ofertas = []

    for fila in filas:
        ofertas.append({
            "id": fila[0],
            "titulo": fila[1],
            "descripcion": fila[2],
            "ciudad": fila[3],
            "precio": float(fila[4]),
            "imagen_url": fila[5],
            "activa": bool(fila[6])
        })

    cursor.close()
    conn.close()

    return ofertas