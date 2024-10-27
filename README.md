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
