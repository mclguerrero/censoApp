import logging
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, timedelta
from ..models import (
    Zona, Localidad, TipoIdentificacion, TipoGenero, TipoEstadoCivil, 
    TipoEscolaridad, TipoProfesion, Usuario, Evento, UsuarioEvento
)

# Configuración del logger
logger = logging.getLogger(__name__)

class UsuarioModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        logger.info("Configurando datos para UsuarioModelTests...")
        zona = Zona.objects.create(nombre="Zona 1", codigo="Z1")
        localidad = Localidad.objects.create(zona=zona, nombre="Localidad 1")
        tipo_identificacion = TipoIdentificacion.objects.create(nombre="Cédula", codigo="CC")
        genero = TipoGenero.objects.create(nombre="Masculino", codigo="M")
        estado_civil = TipoEstadoCivil.objects.create(nombre="Soltero", codigo="SO")
        escolaridad = TipoEscolaridad.objects.create(nombre="Bachillerato", codigo="BA")
        profesion = TipoProfesion.objects.create(nombre="Ingeniero", codigo="IN")
        user = User.objects.create(username="testuser")

        cls.usuario = Usuario.objects.create(
            user=user, nombres="Juan", apellidos="Pérez", n_documento="123456789",
            fecha_nacimiento=date(2000, 1, 1), zona=zona, localidad=localidad, 
            identificacion=tipo_identificacion, genero=genero, estadoCivil=estado_civil,
            escolaridad=escolaridad, profesion=profesion
        )
        logger.info("Datos de prueba para UsuarioModelTests configurados correctamente.")

    def test_calcular_edad(self):
        logger.info("Probando cálculo de edad para el usuario...")
        edad = self.usuario.calcular_edad()
        expected_edad = date.today().year - self.usuario.fecha_nacimiento.year
        if (date.today().month, date.today().day) < (self.usuario.fecha_nacimiento.month, self.usuario.fecha_nacimiento.day):
            expected_edad -= 1
        logger.info(f"Edad calculada: {edad}, Edad esperada: {expected_edad}")
        self.assertEqual(edad, expected_edad)
        logger.info("Prueba de cálculo de edad completada con éxito.")

    def test_usuario_creacion_fallida(self):
        logger.info("Probando creación de usuario con datos faltantes...")
        with self.assertRaises(IntegrityError):
            Usuario.objects.create(user=None, nombres="", apellidos="Pérez")  # Datos incompletos
        logger.info("Prueba de creación fallida completada con éxito.")

    def test_calcular_edad_bisiesto(self):
        logger.info("Probando cálculo de edad para un usuario nacido en un año bisiesto...")
        usuario_bisiesto = Usuario.objects.create(
            user=User.objects.create(username="bisiesto"),
            nombres="Leap",
            apellidos="Year",
            n_documento="987654321",
            fecha_nacimiento=date(2000, 2, 29),  # Fecha bisiesta
            zona=self.usuario.zona,
            localidad=self.usuario.localidad,
            identificacion=self.usuario.identificacion,
            genero=self.usuario.genero,
            estadoCivil=self.usuario.estadoCivil,
            escolaridad=self.usuario.escolaridad,
            profesion=self.usuario.profesion
        )
        edad = usuario_bisiesto.calcular_edad()
        expected_edad = date.today().year - usuario_bisiesto.fecha_nacimiento.year
        if (date.today().month, date.today().day) < (usuario_bisiesto.fecha_nacimiento.month, usuario_bisiesto.fecha_nacimiento.day):
            expected_edad -= 1
        self.assertEqual(edad, expected_edad)
        logger.info("Prueba de cálculo de edad para año bisiesto completada con éxito.")

class UsuarioEventoTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        logger.info("Configurando datos para UsuarioEventoTests...")
        zona = Zona.objects.create(nombre="Zona 1", codigo="Z1")
        localidad = Localidad.objects.create(zona=zona, nombre="Localidad 1")
        tipo_identificacion = TipoIdentificacion.objects.create(nombre="Cédula", codigo="CC")
        genero = TipoGenero.objects.create(nombre="Masculino", codigo="M")
        user = User.objects.create(username="testuser")
        cls.usuario = Usuario.objects.create(
            user=user, nombres="Carlos", apellidos="Gómez", n_documento="123456789",
            fecha_nacimiento=date(1995, 5, 15), zona=zona, localidad=localidad, 
            identificacion=tipo_identificacion, genero=genero
        )
        cls.evento = Evento.objects.create(
            nombre="Evento Test", fecha_inicio=date.today(), fecha_fin=date.today() + timedelta(days=1)
        )
        logger.info("Datos de prueba para UsuarioEventoTests configurados correctamente.")

    def test_evento_duracion_dias(self):
        logger.info("Probando cálculo de duración del evento...")
        duracion = self.evento.duracion_dias
        logger.info(f"Duración calculada: {duracion} días, Duración esperada: 2 días")
        self.assertEqual(duracion, 2)
        logger.info("Prueba de duración del evento completada con éxito.")

    def test_usuarioevento_unicidad(self):
        logger.info("Probando unicidad de asistencia del usuario al evento...")
        UsuarioEvento.objects.create(usuario=self.usuario, evento=self.evento, fecha_asistencia=date.today())
        with self.assertRaises(IntegrityError):  # Asegúrate de usar la excepción correcta
            UsuarioEvento.objects.create(usuario=self.usuario, evento=self.evento, fecha_asistencia=date.today())
        logger.info("Prueba de unicidad de asistencia completada con éxito.")

# Considera implementar pruebas de integración que verifiquen el comportamiento de varios modelos trabajando juntos.
