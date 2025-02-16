# tests/test_customer.py
"""
Módulo de pruebas para la clase Customer.
"""

import unittest
import os
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Clase de pruebas unitarias para Customer."""

    def setUp(self):
        """Configura el entorno de prueba para cada test."""
        self.test_file = "data/test_customers_data.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Limpia el entorno de prueba después de cada test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_customer(self):
        """Prueba la creación de un cliente y la detección de duplicados."""
        c = Customer("C001", "Test Customer", "555-1234", "test@mail.com")
        result = Customer.create_customer(self.test_file, c)
        self.assertTrue(result)

        c2 = Customer("C001", "Other", "333-3333", "dup@mail.com")
        result2 = Customer.create_customer(self.test_file, c2)
        self.assertFalse(result2)

    def test_delete_customer(self):
        """Prueba la eliminación de un cliente."""
        c = Customer("C002", "DeleteMe", "444-4444", "del@mail.com")
        Customer.create_customer(self.test_file, c)
        res = Customer.delete_customer(self.test_file, "C002")
        self.assertTrue(res)
        res2 = Customer.delete_customer(self.test_file, "C002")
        self.assertFalse(res2)

    def test_modify_customer_info(self):
        """Prueba la modificación de la información de un cliente."""
        c = Customer("C003", "ChangeName", "111-1111", "change@mail.com")
        changed = c.modify_customer_info(new_name="NewName", new_phone="999-9999")
        self.assertTrue(changed)
        self.assertEqual(c.name, "NewName")
        self.assertEqual(c.phone, "999-9999")


if __name__ == '__main__':
    unittest.main()
