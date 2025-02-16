#pylint: disable=R0801
# tests/test_reservation.py
"""
Módulo de pruebas para la clase Reservation.
"""
#pylint: disable=R0801
import unittest
import os
from reservation import Reservation
from hotel import Hotel
from customer import Customer


class TestReservation(unittest.TestCase):
    """Clase de pruebas unitarias para Reservation."""

    def setUp(self):
        """Configura el entorno de prueba para cada test."""
        self.res_file = "data/test_reservations_data.txt"
        self.hotel_file = "data/test_hotels_data.txt"
        self.cust_file = "data/test_customers_data.txt"

        for f in [self.res_file, self.hotel_file, self.cust_file]:
            if os.path.exists(f):
                os.remove(f)

        h = Hotel("H10", "TestHotel", "TestCity", 2)
        Hotel.create_hotel(self.hotel_file, h)

        c = Customer("C10", "Test Customer", "555-5555", "test@ex.com")
        Customer.create_customer(self.cust_file, c)

    def tearDown(self):
        """Limpia el entorno de prueba después de cada test."""
        for f in [self.res_file, self.hotel_file, self.cust_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_create_reservation_ok(self):
        """Prueba la creación exitosa de una reservación."""
        r = Reservation("R10", "H10", "C10", ("2025-01-01", "2025-01-05"))
        result = Reservation.create_reservation(
            self.res_file,
            self.hotel_file,
            self.cust_file,
            r
        )
        self.assertTrue(result)

        hotels = Hotel.load_hotels(self.hotel_file)
        for h in hotels:
            if h.hotel_id == "H10":
                self.assertEqual(h.rooms_available, 1)

    def test_create_reservation_no_hotel(self):
        """Prueba la creación de una reservación con hotel inexistente."""
        r = Reservation("R11", "H99", "C10", ("2025-01-01", "2025-01-05"))
        result = Reservation.create_reservation(
            self.res_file,
            self.hotel_file,
            self.cust_file,
            r
        )
        self.assertFalse(result)

    def test_create_reservation_no_customer(self):
        """Prueba la creación de una reservación con cliente inexistente."""
        r = Reservation("R12", "H10", "C99", ("2025-01-01", "2025-01-05"))
        result = Reservation.create_reservation(
            self.res_file,
            self.hotel_file,
            self.cust_file,
            r
        )
        self.assertFalse(result)

    def test_cancel_reservation(self):
        """Prueba la cancelación de una reservación."""
        r = Reservation("R13", "H10", "C10", ("2025-01-01", "2025-01-05"))
        Reservation.create_reservation(
            self.res_file,
            self.hotel_file,
            self.cust_file,
            r
        )
        canceled = Reservation.cancel_reservation(
            self.res_file, self.hotel_file, "R13"
        )
        self.assertTrue(canceled)

        hotels = Hotel.load_hotels(self.hotel_file)
        for h in hotels:
            if h.hotel_id == "H10":
                self.assertEqual(h.rooms_available, 2)


if __name__ == '__main__':
    unittest.main()
