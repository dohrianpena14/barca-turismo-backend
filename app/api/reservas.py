import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.database.connection import get_connection

def crear_reserva(nombre, email, telefono, oferta_id, cantidad_personas, fecha_reserva, metodo_pago):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT precio FROM ofertas_turisticas WHERE id = %s", (oferta_id,))
    oferta = cursor.fetchone()

    if oferta is None:
        cursor.close()
        conn.close()
        return "La oferta no existe"

    precio = oferta[0]
    total = precio * cantidad_personas

    cursor.execute("""
        INSERT INTO reservas
        (nombre_cliente, email_cliente, telefono, oferta_id, cantidad_personas, fecha_reserva, metodo_pago, total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (nombre, email, telefono, oferta_id, cantidad_personas, fecha_reserva, metodo_pago, total))

    conn.commit()

    cursor.close()
    conn.close()

    return "Reserva creada correctamente"