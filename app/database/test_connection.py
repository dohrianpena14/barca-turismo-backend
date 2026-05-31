from connection import get_connection

try:
    conn = get_connection()

    print("Conexion exitosa con Aiven")

    conn.close()

except Exception as e:
    print("Error:")
    print(e)