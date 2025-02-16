# tests/test_hotel.py
"""
Módulo de pruebas para la clase Hotel.
"""

import unittest
import os
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Clase de pruebas unitarias para Hotel."""

    def setUp(self):
        """Configura el entorno de prueba para cada test."""
        self.test_file = "data/test_hotels_data.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Limpia el entorno de prueba después de cada test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_hotel(self):
        """Prueba la creación de un hotel y la detección de duplicados."""
        h = Hotel("H001", "Test Hotel", "Test City", 10)
        result = Hotel.create_hotel(self.test_file, h)
        self.assertTrue(result)

        h2 = Hotel("H001", "Duplicate Hotel", "Anywhere", 5)
        result2 = Hotel.create_hotel(self.test_file, h2)
        self.assertFalse(result2)

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel."""
        h = Hotel("H002", "Hotel to Delete", "Loc", 5)
        Hotel.create_hotel(self.test_file, h)
        res = Hotel.delete_hotel(self.test_file, "H002")
        self.assertTrue(res)
        res2 = Hotel.delete_hotel(self.test_file, "H002")
        self.assertFalse(res2)

    def test_reserve_room(self):
        """Prueba la reserva de una habitación."""
        h = Hotel("H003", "Res Hotel", "Loc", 2)
        Hotel.create_hotel(self.test_file, h)

        hotels_loaded = Hotel.load_hotels(self.test_file)
        for hotel in hotels_loaded:
            if hotel.hotel_id == "H003":
                r = hotel.reserve_room()
                self.assertTrue(r)
                self.assertEqual(hotel.rooms_available, 1)

    def test_cancel_reservation(self):
        """Prueba la cancelación de una reservación."""
        h = Hotel("H004", "CancelRes Hotel", "Loc", 2)
        Hotel.create_hotel(self.test_file, h)
        h.reserve_room()
        h.cancel_reservation()
        self.assertEqual(h.rooms_available, h.rooms)


if __name__ == '__main__':
    unittest.main()
