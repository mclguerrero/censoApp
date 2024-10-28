# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from ...models import Usuario, Familia, Evento, UsuarioEvento, Localidad, Zona

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = ['id', 'nombre', 'codigo']

class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = ['id', 'nombre', 'zona']

# Serializer de Usuario con creación automática de User
class UsuarioSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        n_documento = validated_data.get('n_documento')
        user, created = User.objects.get_or_create(
            username=n_documento,
            defaults={
                'first_name': validated_data.get('nombres'),
                'last_name': validated_data.get('apellidos'),
                'password': make_password(n_documento)
            }
        )
        if created:
            # Asigna al grupo 'Usuario' si existe
            try:
                group = Group.objects.get(name='Usuario')
                user.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError("Error: el grupo 'Usuario' no existe en el sistema.")
        
        usuario = Usuario.objects.create(user=user, **validated_data)
        return usuario


# Serializer de Familia
class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = ['id', 'nombre', 'direccion', 'telefono', 'correo']


# Serializer de Evento
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = [
            'id', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'duracion_dias',
            'es_favorito', 'imagen'
        ]


# Serializer de UsuarioEvento para gestionar las asistencias
class UsuarioEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEvento
        fields = [
            'id', 'usuario', 'evento', 'fecha_asistencia', 'asistencia'
        ]

    def create(self, validated_data):
        usuario_evento = UsuarioEvento.objects.create(**validated_data)
        return usuario_evento

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'