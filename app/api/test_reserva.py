from reservas import crear_reserva

resultado = crear_reserva(
    "Dohrian Peña",
    "cliente@email.com",
    "8090000000",
    1,
    2,
    "2026-06-15",
    "Tarjeta"
)

print(resultado)