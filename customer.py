# customer.py
"""
Módulo que define la clase Customer y sus métodos
para CRUD y manejo de archivos.
"""

import os


class Customer:
    """
    Representa la información de un cliente.

    Atributos:
        customer_id (str): Identificador único.
        name (str): Nombre del cliente.
        phone (str): Número telefónico.
        email (str): Correo electrónico.
    """

    def __init__(self, customer_id, name, phone, email):
        """
        Inicializa un objeto Customer.

        Args:
            customer_id (str): ID único del cliente.
            name (str): Nombre del cliente.
            phone (str): Teléfono del cliente.
            email (str): Email del cliente.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def display_customer_info(self):
        """Muestra la información del cliente en consola."""
        print(f"Customer ID: {self.customer_id}")
        print(f"Nombre: {self.name}")
        print(f"Teléfono: {self.phone}")
        print(f"Email: {self.email}\n")

    def modify_customer_info(self, new_name=None, new_phone=None, new_email=None):
        """
        Modifica la información del cliente según los parámetros no nulos.

        Args:
            new_name (str, optional): Nuevo nombre.
            new_phone (str, optional): Nuevo teléfono.
            new_email (str, optional): Nuevo email.

        Returns:
            bool: True si se modificó algo, False en caso contrario.
        """
        modified = False
        if new_name is not None:
            self.name = new_name
            modified = True

        if new_phone is not None:
            self.phone = new_phone
            modified = True

        if new_email is not None:
            self.email = new_email
            modified = True

        return modified

    @staticmethod
    def load_customers(filename):
        """
        Carga la lista de clientes desde un archivo de texto.
        Formato esperado: customer_id|nombre|telefono|email

        Args:
            filename (str): Ruta del archivo.

        Returns:
            list: Lista de objetos Customer.
        """
        customers = []
        if not os.path.exists(filename):
            return customers

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cust_id, name, phone, email = line.split('|')
                    c = Customer(cust_id, name, phone, email)
                    customers.append(c)
                except ValueError as err:
                    print(f"[Error] Línea inválida: '{line}'. {err}")
        return customers

    @staticmethod
    def save_customers(filename, customers_list):
        """
        Guarda la lista de clientes en un archivo de texto (sobrescribe).
        Formato: customer_id|nombre|telefono|email

        Args:
            filename (str): Ruta del archivo.
            customers_list (list): Lista de objetos Customer.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            for cust in customers_list:
                line = f"{cust.customer_id}|{cust.name}|{cust.phone}|{cust.email}\n"
                file.write(line)

    @staticmethod
    def create_customer(filename, customer_obj):
        """
        Agrega un nuevo cliente en el archivo.

        Args:
            filename (str): Ruta del archivo.
            customer_obj (Customer): Objeto Customer a agregar.

        Returns:
            bool: True si se agregó, False si existe ID duplicado.
        """
        customers_list = Customer.load_customers(filename)
        for c in customers_list:
            if c.customer_id == customer_obj.customer_id:
                print(f"[Error] Ya existe un cliente con ID '{customer_obj.customer_id}'")
                return False

        customers_list.append(customer_obj)
        Customer.save_customers(filename, customers_list)
        return True

    @staticmethod
    def delete_customer(filename, customer_id):
        """
        Elimina un cliente del archivo por su ID.

        Args:
            filename (str): Ruta del archivo.
            customer_id (str): ID del cliente a eliminar.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        customers_list = Customer.load_customers(filename)
        new_list = [c for c in customers_list if c.customer_id != customer_id]
        if len(new_list) == len(customers_list):
            print(f"[Aviso] No se encontró el Cliente con ID '{customer_id}'.")
            return False

        Customer.save_customers(filename, new_list)
        return True
