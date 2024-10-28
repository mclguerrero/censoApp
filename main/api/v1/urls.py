from rest_framework.routers import DefaultRouter
from .views import ZonaViewSet, LocalidadViewSet, UsuarioViewSet, EventoViewSet, UsuarioEventoViewSet

router = DefaultRouter()
router.register(r'zonas', ZonaViewSet)
router.register(r'localidades', LocalidadViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'usuario_eventos', UsuarioEventoViewSet)

urlpatterns = router.urls