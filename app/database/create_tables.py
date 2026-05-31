from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ofertas_turisticas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    imagen_url VARCHAR(255),
    activa BOOLEAN DEFAULT TRUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cliente VARCHAR(100) NOT NULL,
    email_cliente VARCHAR(150) NOT NULL,
    telefono VARCHAR(30),
    oferta_id INT NOT NULL,
    cantidad_personas INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    metodo_pago VARCHAR(50),
    total DECIMAL(10,2),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (oferta_id) REFERENCES ofertas_turisticas(id)
);
""")

conn.commit()
cursor.close()
conn.close()

print("Tablas creadas correctamente")