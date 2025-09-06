# Message Board

Este proyecto es una aplicación web construida con Django que permite a los usuarios ver y gestionar mensajes en un tablero.

## Estructura del proyecto
- `django_base/`: Configuración principal de Django.
- `message_board/`: Aplicación principal donde se gestionan los mensajes.
- `templates/`: Archivos HTML para la interfaz de usuario.
- `db.sqlite3`: Base de datos SQLite utilizada por Django.
- `manage.py`: Script para gestionar el proyecto.
- `requirements.txt`: Dependencias del proyecto.

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
4. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso
Accede a `http://127.0.0.1:8000/` en tu navegador para ver el tablero de mensajes.

## Licencia
Este proyecto está bajo la licencia MIT.
