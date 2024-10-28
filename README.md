# Proyecto Censo

## Introducción

El proyecto es una aplicación web desarrollada en **Django** que permite la gestión eficiente de eventos y usuarios. Esta aplicación ofrece una interfaz de usuario intuitiva basada en plantillas HTML, facilitando la administración de eventos y la autenticación de usuarios.

## Tecnologías Utilizadas

- **Python**
- **Django**
- **MySQL**

## Instalación

### Pasos de Instalación

Sigue los siguientes pasos para instalar y configurar el proyecto:

1. **Clona el repositorio**

   Abre tu terminal y ejecuta los siguientes comandos:

   ```bash
   git clone https://github.com/mclguerrero/censoApp.git

   ```
   ```bash
   cd censoApp
   ```

2. **Crea y activa un entorno virtual**

   Crea un entorno virtual y actívalo con los siguientes comandos:

   ```bash
   python -m venv env
   ```
   ```bash
   env\Scripts\activate
   ```
   - **¿Error al activar el entorno virtual?**

     Si experimentas un error al intentar activar el entorno virtual, abre PowerShell como administrador y ejecuta:

     ```bash
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```

     Luego, cierra PowerShell.

3. **Instala las dependencias**

   Instala todas las dependencias necesarias listadas en el archivo `requirements.txt` ejecutando:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos en .env**

- En el directorio raíz del proyecto, crea un archivo llamado `.env`.
- Dentro del archivo `.env`, añade las siguientes variables de configuración, reemplazando los valores de ejemplo según tu configuración local:

 ```bash
  DB_NAME=censo_bd
  DB_USER=root
  DB_PASSWORD=root
  DB_HOST=localhost
  DB_PORT=3306
```  

   - **DB_NAME**: Nombre de la base de datos que usará la aplicación.
   - **DB_USER**: Usuario de la base de datos.
   - **DB_PASSWORD**: Contraseña del usuario de la base de datos.
   - **DB_HOST**: Dirección del servidor de la base de datos (usualmente `localhost` para desarrollo local).
   - **DB_PORT**: Puerto de conexión a la base de datos (ejemplo: `3306` para MySQL).

Este archivo es fundamental para el correcto funcionamiento de la aplicación, ya que provee las credenciales necesarias para la conexión con la base de datos.

5. **Aplica las migraciones**

   Ejecuta los siguientes comandos para aplicar las migraciones:

   ```bash
   python manage.py makemigrations 
   ```
   ```bash
   python manage.py migrate
   ```

6. **Inicia el servidor de desarrollo**

   Para iniciar el servidor de desarrollo, utiliza el siguiente comando:

   ```bash
   python manage.py runserver
   ```

7. **Pruebas Unitarias**

Este proyecto cuenta con pruebas unitarias para asegurar el correcto funcionamiento de formularios y modelos.

   - **Ejecución de Pruebas**
Para ejecutar las pruebas unitarias de formularios y modelos, utiliza los siguientes comandos:

  ```bash
  python manage.py test main.tests.test_forms --verbosity 2
  ```
  ```bash
  python manage.py test main.tests.test_models --verbosity 2
  ```
8. **API**

Esta API proporciona un acceso programático a los recursos de la aplicación, permitiendo a los administradores gestionar los datos de manera eficiente.
   - **1. Autenticación**

La API utiliza autenticación basada en tokens. Para acceder a los endpoints protegidos, se requiere un token de autenticación que se debe incluir en los encabezados de las solicitudes.

**Ejemplo de encabezado de autorización:**
```http
Authorization: Token 1234567890abcdef1234567890abcdef12345678
```
   - **2. Endpoints de la API**

### Usuarios

- **Lista de Usuarios**
  - `GET /api/v1/usuarios/`
  - **Permisos:** Solo administradores.
  
- **Crear Usuario**
  - `POST /api/v1/usuarios/`
  - **Permisos:** Solo administradores.
  
- **Actualizar Usuario**
  - `PUT /api/v1/usuarios/{id}/`
  - **Permisos:** Solo administradores.
  
- **Eliminar Usuario**
  - `DELETE /api/v1/usuarios/{id}/`
  - **Permisos:** Solo administradores.

### Zonas

- **Lista de Zonas**
  - `GET /api/v1/zonas/`
  - **Permisos:** Solo administradores.
  
- **Crear Zona**
  - `POST /api/v1/zonas/`
  - **Permisos:** Solo administradores.
  
- **Actualizar Zona**
  - `PUT /api/v1/zonas/{id}/`
  - **Permisos:** Solo administradores.
  
- **Eliminar Zona**
  - `DELETE /api/v1/zonas/{id}/`
  - **Permisos:** Solo administradores.

### Localidades

- **Lista de Localidades**
  - `GET /api/v1/localidades/`
  - **Permisos:** Solo administradores.
  
- **Crear Localidad**
  - `POST /api/v1/localidades/`
  - **Permisos:** Solo administradores.
  
- **Actualizar Localidad**
  - `PUT /api/v1/localidades/{id}/`
  - **Permisos:** Solo administradores.
  
- **Eliminar Localidad**
  - `DELETE /api/v1/localidades/{id}/`
  - **Permisos:** Solo administradores.

### Eventos

- **Lista de Eventos**
  - `GET /api/v1/eventos/`
  - **Permisos:** Solo administradores.
  
- **Crear Evento**
  - `POST /api/v1/eventos/`
  - **Permisos:** Solo administradores.
  
- **Actualizar Evento**
  - `PUT /api/v1/eventos/{id}/`
  - **Permisos:** Solo administradores.
  
- **Eliminar Evento**
  - `DELETE /api/v1/eventos/{id}/`
  - **Permisos:** Solo administradores.

### UsuarioEventos

- **Lista de UsuarioEventos**
  - `GET /api/v1/usuario-eventos/`
  - **Permisos:** Solo administradores.
  
- **Crear UsuarioEvento**
  - `POST /api/v1/usuario-eventos/`
  - **Permisos:** Solo administradores.
  
- **Actualizar UsuarioEvento**
  - `PUT /api/v1/usuario-eventos/{id}/`
  - **Permisos:** Solo administradores.
  
- **Eliminar UsuarioEvento**
  - `DELETE /api/v1/usuario-eventos/{id}/`
  - **Permisos:** Solo administradores.


 - **4. Permisos**
Los permisos de acceso están configurados para que solo los usuarios que pertenecen al grupo "Admin" puedan realizar operaciones de creación, actualización y eliminación. Esto se gestiona a través de las clases de permisos de Django REST Framework (`IsAuthenticated`, `IsAdminUser`, `DjangoModelPermissions`).

 - **5. Ejemplos de Uso**

### Obtener la lista de Localidades

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/localidades/' \
  -H 'accept: application/json' \
  -H 'X-CSRFTOKEN: 1234567890abcdef1234567890abcdef12345678'
```

### Crear un nuevo Localidades

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/localidades/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFTOKEN: 1234567890abcdef1234567890abcdef12345678' \
  -d '{
  "nombre": "string",
  "zona": 1
}'
```

## 6. Errores Comunes

- **403 Forbidden**: Este error indica que el usuario no tiene permisos para realizar la acción solicitada. Asegúrate de que el usuario pertenezca al grupo "Admin" y tenga los permisos necesarios.
- **404 Not Found**: Este error indica que la URL solicitada no fue encontrada. Verifica que estés utilizando el endpoint correcto.
