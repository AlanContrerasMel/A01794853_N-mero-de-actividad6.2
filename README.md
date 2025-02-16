Este repositorio contiene la implementación de un Sistema de Reservaciones en Python, desarrollado como parte de la actividad 6.2 de Pruebas de Software. El proyecto incluye la definición de clases para la gestión de hoteles, clientes y reservaciones, junto con pruebas unitarias para garantizar la calidad y el correcto funcionamiento del sistema. Además, se ha verificado el cumplimiento de los estándares de PEP8 y se han utilizado herramientas como flake8 y PyLint para asegurar un código limpio.

Características
Gestión de Hoteles:
Permite crear, modificar, mostrar, reservar habitaciones y eliminar hoteles, utilizando archivos de texto para la persistencia.

Gestión de Clientes:
Permite crear, modificar, mostrar y eliminar clientes, guardando la información en archivos.

Gestión de Reservaciones:
Permite crear y cancelar reservaciones, validando que el hotel y el cliente existan y que haya disponibilidad en el hotel.

Pruebas Unitarias:
Se han implementado casos de prueba usando el módulo unittest para asegurar la correcta ejecución de las funcionalidades del sistema. La cobertura de código supera el 85%.

Cumplimiento de Estándares:
El código cumple con PEP8 y no genera errores o advertencias significativas al ser analizado con flake8 y PyLint.

MatriculaEstudiante_ActividadA6.2/
├── customer.py              # Definición de la clase Customer
├── hotel.py                 # Definición de la clase Hotel
├── reservation.py           # Definición de la clase Reservation
├── main.py                  # Script principal para demostrar el funcionamiento
├── tests/                   # Casos de prueba con unittest
│   ├── __init__.py
│   ├── test_customer.py
│   ├── test_hotel.py
│   └── test_reservation.py
├── data/                    # Archivos de datos para persistencia
│   ├── customers_data.txt
│   ├── hotels_data.txt
│   └── reservations_data.txt
├── .flake8                 # Configuración de flake8
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo


Instalar las dependencias:
    pip install -r requirements.txt

Uso
    Para ejecutar la demostración del sistema, ejecutar:
        python main.py

El script main.py crea un hotel, un cliente y una reservación de ejemplo, mostrando en consola el funcionamiento de las operaciones.

Pruebas y Cobertura
    Ejecutar pruebas unitarias:

        Desde la raíz del proyecto, ejecutar:

            coverage run -m unittest discover -s tests
            coverage report -m
                
                Esto te mostrará un reporte de la cobertura de código, que debe ser superior al 85%.

Verificar el estilo del código con flake8:

    flake8 .

Verificar el código con PyLint:

    pylint hotel.py customer.py reservation.py main.py tests/

Notas
El proyecto utiliza archivos de texto en la carpeta data/ para guardar la información de hoteles, clientes y reservaciones. Asegúrate de que estos archivos existan (pueden estar vacíos inicialmente) o se generarán automáticamente al ejecutar las funciones de creación.
Si se producen mensajes de error o aviso en la consola, son parte de la gestión de casos especiales (por ejemplo, intento de crear duplicados o eliminar registros inexistentes).