from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from main.models import Usuario, Zona, Localidad, Evento, UsuarioEvento
from .serializers import ZonaSerializer, LocalidadSerializer, UsuarioSerializer, EventoSerializer, UsuarioEventoSerializer
from main.permissions import IsAdminGroup

class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer
    permission_classes = [IsAuthenticated, IsAdminGroup]  

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = [IsAuthenticated, IsAdminGroup]  

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminGroup]  

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated, IsAdminGroup]  

class UsuarioEventoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioEvento.objects.all()
    serializer_class = UsuarioEventoSerializer
    permission_classes = [IsAuthenticated, IsAdminGroup]  