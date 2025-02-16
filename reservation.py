# reservation.py
"""
Módulo que define la clase Reservation y sus métodos
para CRUD y manejo de archivos.
"""

import os
from hotel import Hotel
from customer import Customer


class Reservation:
    """
    Representa una reservación.

    Atributos:
        reservation_id (str): ID único.
        hotel_id (str): ID del hotel.
        customer_id (str): ID del cliente.
        check_in (str): Fecha de llegada.
        check_out (str): Fecha de salida.
    """

    def __init__(self, reservation_id, hotel_id, customer_id, dates):
        """
        Inicializa una reservación.

        Args:
            reservation_id (str): ID de la reservación.
            hotel_id (str): ID del hotel.
            customer_id (str): ID del cliente.
            dates (tuple): Tupla que contiene (check_in, check_out).
        """
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id
        self.check_in, self.check_out = dates

    @staticmethod
    def load_reservations(filename):
        """
        Carga las reservaciones desde un archivo de texto.
        Formato: reservation_id|hotel_id|customer_id|check_in|check_out

        Args:
            filename (str): Ruta del archivo.

        Returns:
            list: Lista de objetos Reservation.
        """
        reservations = []
        if not os.path.exists(filename):
            return reservations

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    rid, hid, cid, cin, cout = line.split('|')
                    r = Reservation(rid, hid, cid, (cin, cout))
                    reservations.append(r)
                except ValueError as err:
                    print(f"[Error] Datos inválidos: '{line}'. {err}")
        return reservations

    @staticmethod
    def save_reservations(filename, reservations_list):
        """
        Guarda la lista de reservaciones en un archivo de texto.
        Sobrescribe el contenido anterior.

        Args:
            filename (str): Ruta del archivo.
            reservations_list (list): Lista de objetos Reservation.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            for r in reservations_list:
                line = f"{r.reservation_id}|{r.hotel_id}|{r.customer_id}|"
                line += f"{r.check_in}|{r.check_out}\n"
                file.write(line)

    @staticmethod
    def create_reservation(filename_res, filename_hotels, filename_cust, reservation_obj):
        """
        Crea una reservación si el Hotel y el Cliente existen y hay habitaciones disponibles.
        Actualiza la disponibilidad del hotel y guarda la reservación.

        Args:
            filename_res (str): Archivo de reservaciones.
            filename_hotels (str): Archivo de hoteles.
            filename_cust (str): Archivo de clientes.
            reservation_obj (Reservation): Objeto Reservation a crear.

        Returns:
            bool: True si la operación es exitosa, False en caso de error.
        """
        hotels = Hotel.load_hotels(filename_hotels)
        customers = Customer.load_customers(filename_cust)

        target_hotel = None
        for h in hotels:
            if h.hotel_id == reservation_obj.hotel_id:
                target_hotel = h
                break
        if not target_hotel:
            print(f"[Error] El hotel {reservation_obj.hotel_id} no existe.")
            return False

        target_customer = None
        for c in customers:
            if c.customer_id == reservation_obj.customer_id:
                target_customer = c
                break
        if not target_customer:
            print(f"[Error] El cliente {reservation_obj.customer_id} no existe.")
            return False

        if not target_hotel.reserve_room():
            print("[Error] No hay habitaciones disponibles.")
            return False

        existing_res = Reservation.load_reservations(filename_res)
        for r in existing_res:
            if r.reservation_id == reservation_obj.reservation_id:
                print(f"[Error] La reservación {reservation_obj.reservation_id} ya existe.")
                target_hotel.cancel_reservation()
                return False

        existing_res.append(reservation_obj)
        Reservation.save_reservations(filename_res, existing_res)
        Hotel.save_hotels(filename_hotels, hotels)
        return True

    @staticmethod
    def cancel_reservation(filename_res, filename_hotels, reservation_id):
        """
        Cancela una reservación dada por su ID.
        Restaura la habitación en el hotel correspondiente y guarda los cambios.

        Args:
            filename_res (str): Archivo de reservaciones.
            filename_hotels (str): Archivo de hoteles.
            reservation_id (str): ID de la reservación a cancelar.

        Returns:
            bool: True si se canceló, False si no se encontró la reservación.
        """
        res_list = Reservation.load_reservations(filename_res)
        to_cancel = None
        for r in res_list:
            if r.reservation_id == reservation_id:
                to_cancel = r
                break

        if not to_cancel:
            print(f"[Aviso] No se encontró la reservación '{reservation_id}'.")
            return False

        hotels = Hotel.load_hotels(filename_hotels)
        for h in hotels:
            if h.hotel_id == to_cancel.hotel_id:
                h.cancel_reservation()
                break

        new_res_list = [r for r in res_list if r.reservation_id != reservation_id]
        Reservation.save_reservations(filename_res, new_res_list)
        Hotel.save_hotels(filename_hotels, hotels)
        return True
