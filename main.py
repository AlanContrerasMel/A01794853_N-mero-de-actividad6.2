# main.py
"""
Módulo principal para ejecutar el sistema de reservaciones.
"""

from hotel import Hotel
from customer import Customer
from reservation import Reservation


def main():
    """
    Ejecuta una demostración de las operaciones principales del sistema de reservaciones.
    """
    hotel_file = "data/hotels_data.txt"
    cust_file = "data/customers_data.txt"
    res_file = "data/reservations_data.txt"

    print("=== DEMO: Creación de Hotel ===")
    h1 = Hotel("H100", "Hotel Central", "Ciudad", 5)
    creado = Hotel.create_hotel(hotel_file, h1)
    if creado:
        print("Hotel creado correctamente.\n")

    print("=== DEMO: Creación de Cliente ===")
    c1 = Customer("C200", "Juan Pérez", "555-1234", "juan@example.com")
    creado = Customer.create_customer(cust_file, c1)
    if creado:
        print("Cliente creado correctamente.\n")

    print("=== DEMO: Creación de Reservación ===")
    # Se pasa una tupla para las fechas: (check_in, check_out)
    r1 = Reservation("R300", "H100", "C200", ("2025-03-10", "2025-03-15"))
    ok = Reservation.create_reservation(res_file, hotel_file, cust_file, r1)
    if ok:
        print("Reservación creada con éxito.\n")

    print("=== Mostrar información Hotel (H100) ===")
    hoteles = Hotel.load_hotels(hotel_file)
    for h in hoteles:
        if h.hotel_id == "H100":
            h.display_info()

    print("=== Cancelar la reservación 'R300' ===")
    cancelado = Reservation.cancel_reservation(res_file, hotel_file, "R300")
    if cancelado:
        print("Se canceló la reservación R300. Habitación restaurada.\n")

    print("=== FIN DEMO ===")


if __name__ == "__main__":
    main()
