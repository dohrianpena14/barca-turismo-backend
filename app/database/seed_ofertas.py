from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

ofertas = [
    ("Tour Spotify Camp Nou", "Recorrido por zonas históricas del Barça.", "Barcelona", 35.00, "campnou.jpg"),
    ("Museo FC Barcelona", "Visita al museo con trofeos y experiencias interactivas.", "Barcelona", 25.00, "museo.jpg"),
    ("Experiencia VIP Barça", "Tour premium inspirado en días de partido.", "Barcelona", 120.00, "vip.jpg"),
]

cursor.executemany("""
INSERT INTO ofertas_turisticas 
(titulo, descripcion, ciudad, precio, imagen_url)
VALUES (%s, %s, %s, %s, %s)
""", ofertas)

conn.commit()
cursor.close()
conn.close()

print("Ofertas insertadas correctamente")