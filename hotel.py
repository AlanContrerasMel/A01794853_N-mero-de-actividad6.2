# hotel.py
"""
Módulo que define la clase Hotel y sus métodos
para CRUD y manejo de archivos.
"""

import os


class Hotel:
    """
    Representa la información de un hotel.

    Atributos:
        hotel_id (str): identificador único del hotel.
        name (str): nombre del hotel.
        location (str): ubicación del hotel.
        rooms (int): número total de habitaciones.
        rooms_available (int): habitaciones disponibles.
    """

    def __init__(self, hotel_id, name, location, rooms):
        """
        Inicializa un objeto Hotel.

        Args:
            hotel_id (str): Identificador único del hotel.
            name (str): Nombre del hotel.
            location (str): Ubicación del hotel.
            rooms (int): Número total de habitaciones.
        """
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = int(rooms)
        self.rooms_available = int(rooms)

    def display_info(self):
        """Muestra la información del hotel en consola."""
        print(f"Hotel ID: {self.hotel_id}")
        print(f"Nombre: {self.name}")
        print(f"Ubicación: {self.location}")
        print(f"Habitaciones totales: {self.rooms}")
        print(f"Habitaciones disponibles: {self.rooms_available}\n")

    def modify_info(self, new_name=None, new_location=None, new_rooms=None):
        """
        Modifica los datos del hotel según los parámetros no nulos.

        Args:
            new_name (str, optional): Nuevo nombre.
            new_location (str, optional): Nueva ubicación.
            new_rooms (int, optional): Nuevo total de habitaciones.

        Returns:
            bool: True si se modificó algo, False en caso contrario.
        """
        modified = False

        if new_name is not None:
            self.name = new_name
            modified = True

        if new_location is not None:
            self.location = new_location
            modified = True

        if new_rooms is not None:
            difference = int(new_rooms) - self.rooms
            self.rooms = int(new_rooms)
            self.rooms_available += difference
            self.rooms_available = max(self.rooms_available, 0)
            modified = True

        return modified

    def reserve_room(self):
        """
        Reserva una habitación, reduciendo rooms_available en 1,
        si hay al menos una habitación libre.

        Returns:
            bool: True si se pudo reservar, False en caso contrario.
        """
        if self.rooms_available > 0:
            self.rooms_available -= 1
            return True
        return False

    def cancel_reservation(self):
        """
        Cancela una reservación, incrementando las habitaciones disponibles
        si no excede el total.
        """
        if self.rooms_available < self.rooms:
            self.rooms_available += 1

    @staticmethod
    def load_hotels(filename):
        """
        Carga la lista de hoteles desde un archivo de texto.
        El formato esperado es:
        hotel_id|nombre|ubicacion|rooms|rooms_available

        Args:
            filename (str): Ruta del archivo.

        Returns:
            list: Lista de objetos Hotel.
        """
        hotels = []
        if not os.path.exists(filename):
            return hotels

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    hotel_id, name, location, rooms, rooms_avail = line.split('|')
                    h = Hotel(hotel_id, name, location, rooms)
                    h.rooms_available = int(rooms_avail)
                    hotels.append(h)
                except ValueError as err:
                    print(f"[Error] Datos inválidos en línea: '{line}'. Error: {err}")
        return hotels

    @staticmethod
    def save_hotels(filename, hotels_list):
        """
        Guarda la lista de hoteles en un archivo de texto.
        Sobrescribe el contenido anterior.

        Args:
            filename (str): Ruta del archivo.
            hotels_list (list): Lista de objetos Hotel.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            for hotel in hotels_list:
                line = f"{hotel.hotel_id}|{hotel.name}|{hotel.location}|"
                line += f"{hotel.rooms}|{hotel.rooms_available}\n"
                file.write(line)

    @staticmethod
    def create_hotel(filename, hotel_obj):
        """
        Crea un hotel y lo agrega al archivo de hoteles.

        Args:
            filename (str): Ruta del archivo.
            hotel_obj (Hotel): Objeto Hotel a agregar.

        Returns:
            bool: True si se guarda correctamente, False si ya existe un ID igual.
        """
        hotels_list = Hotel.load_hotels(filename)
        for h in hotels_list:
            if h.hotel_id == hotel_obj.hotel_id:
                print(f"[Error] Ya existe un Hotel con ID '{hotel_obj.hotel_id}'")
                return False

        hotels_list.append(hotel_obj)
        Hotel.save_hotels(filename, hotels_list)
        return True

    @staticmethod
    def delete_hotel(filename, hotel_id):
        """
        Elimina un hotel del archivo por su ID.

        Args:
            filename (str): Ruta del archivo.
            hotel_id (str): ID del hotel a eliminar.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        hotels_list = Hotel.load_hotels(filename)
        new_list = [h for h in hotels_list if h.hotel_id != hotel_id]
        if len(new_list) == len(hotels_list):
            print(f"[Aviso] No se encontró el Hotel con ID '{hotel_id}'.")
            return False

        Hotel.save_hotels(filename, new_list)
        return True
