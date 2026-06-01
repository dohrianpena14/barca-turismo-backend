from fastapi import FastAPI
from routes import obtener_ofertas
from reservas import crear_reserva

api = FastAPI()

@api.get("/ofertas")
def get_ofertas():
    return obtener_ofertas()

@api.post("/reservas")
def post_reserva(
    nombre: str,
    email: str,
    telefono: str,
    oferta_id: int,
    cantidad_personas: int,
    fecha_reserva: str,
    metodo_pago: str
):
    return crear_reserva(
        nombre,
        email,
        telefono,
        oferta_id,
        cantidad_personas,
        fecha_reserva,
        metodo_pago
    )