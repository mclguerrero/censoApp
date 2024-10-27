from django.test import TestCase
from django import forms
from django.contrib.auth.models import User
from datetime import date
from ..models import (
    Zona, Localidad, TipoIdentificacion, TipoGenero, TipoEstadoCivil,
    TipoEscolaridad, TipoProfesion, Usuario, Evento
)
from ..forms import UsuarioForm, EventoForm  # Ensure your forms are imported
from django.utils.timezone import timedelta


class UsuarioFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.zona = Zona.objects.create(nombre="Zona 1", codigo="Z1")
        cls.localidad = Localidad.objects.create(zona=cls.zona, nombre="Localidad 1")
        cls.tipo_identificacion = TipoIdentificacion.objects.create(nombre="Cédula", codigo="CC")
        cls.genero = TipoGenero.objects.create(nombre="Masculino", codigo="M")
        cls.estado_civil = TipoEstadoCivil.objects.create(nombre="Soltero", codigo="S")
        cls.escolaridad = TipoEscolaridad.objects.create(nombre="Secundaria", codigo="SEC")
        cls.profesion = TipoProfesion.objects.create(nombre="Ingeniero", codigo="ING")
        cls.user = User.objects.create(username="testuser")

    def test_usuario_form_valid_data(self):
        form_data = {
            'user': self.user.id,
            'nombres': "Juan",
            'apellidos': "Perez",
            'n_documento': "1234567890",
            'fecha_nacimiento': date(2000, 1, 1),
            'zona': self.zona.id,
            'localidad': self.localidad.id,
            'direccion': "Calle #8",
            'telefono': "1234567890",
            'identificacion': self.tipo_identificacion.id,
            'genero': self.genero.id,
            'estadoCivil': self.estado_civil.id,
            'escolaridad': self.escolaridad.id,
            'profesion': self.profesion.id,
        }
        form = UsuarioForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Errores encontrados: {form.errors}")

    def test_usuario_form_invalid_data(self):
        form_data = {
            'user': self.user.id,
            'nombres': "123",  # Empty name should make the form invalid
            'apellidos': "123",
            'n_documento': "123",  # Invalid document number
            'fecha_nacimiento': date(2000, 1, 1),
            'zona': self.zona.id,
            'localidad': self.localidad.id,
            'direccion': "Calle #8",
            'telefono': "1234567890",
            'identificacion': self.tipo_identificacion.id,
            'genero': self.genero.id,
            'estadoCivil': self.estado_civil.id,
            'escolaridad': self.escolaridad.id,
            'profesion': self.profesion.id,
        }
        form = UsuarioForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nombres', form.errors)


class EventoFormTests(TestCase):

    def test_evento_form_valid_data(self):
        form_data = {
            'nombre': "Evento Test",
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=1),
            'es_favorito': True,
        }
        form = EventoForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Errores encontrados: {form.errors}")

    def test_evento_form_invalid_dates(self):
        form_data = {
            'nombre': "Evento Test",
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() - timedelta(days=1),  # End date before start date
        }
        form = EventoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('fecha_fin', form.errors)
