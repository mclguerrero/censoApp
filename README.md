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

4. **Configura la base de datos**

   Asegúrate de configurar correctamente tu base de datos en el archivo `settings.py`.

5. **Aplica las migraciones**

   Ejecuta los siguientes comandos para aplicar las migraciones:

   ```bash
   python manage.py makemigrations 
   python manage.py migrate
   ```

6. **Inicia el servidor de desarrollo**

   Para iniciar el servidor de desarrollo, utiliza el siguiente comando:

   ```bash
   python manage.py runserver
   ```