Nutriología API
====================

## Requirements

* Python 3.12+
* Pip (23.3.2) - 3.12+
* MySQL 8.4+

## Setup 

1. Clonar el Proyecto e Ingresar

2. Crear Ambiente Virtual con Python `virtualenv`
- Linux: `$ python -m env {venv-name}`
- Windows: `> python -m venv {venv-name}`

3. Activar el Ambiente Virtual
- Linux: `$ source env/bin/activate`
- Windows: `C:/path_to_the_folder/ > .\venv-name\Scripts\activate`

## Development Server

1. Instalar las Librerías Requeridas
- `$ pip install -r requirements.txt`

2. Crear la Base de Datos en MySQL con el Nombre Establecido en `my.cnf`
3. Si MySQL Está Configurado con Usuario y Contraseña Personalizados, Establecer los Párametros en `my.cnf` 

4. Aplicar las Migraciones de Django
- `$ python manage.py migrate`
- `$ python manage.py makemigrations nutriologia`
- `$ python manage.py migrate`

6. Crear Superusuario
- `$ python manage.py createsuperuser`

7. Correr el Servidor
- `$ python manage.py runserver`

## Django Administration

- URL: `http://127.0.0.1:8000/admin`
