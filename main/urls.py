# urls

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CensoApp API",
        default_version='v1',
        description="Documentación de la API",
        contact=openapi.Contact(email="soporte@censoapp.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('api/v1/', include('main.api.v1.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),

    #select2

    path("select2/", include("django_select2.urls")),

    #rol user

    path('myData/', views.ver_infopersonal, name='ver_infopersonal'),
    path('myFamily/', views.ver_mifamilia, name='ver_mifamilia'),

    #usuarios

    path('user/new/', views.crear_usuario, name='crear_usuario'),
    path('users/', views.listar_usuarios, name='listar_usuarios'),
    path('user/<int:pk>/edit/', views.actualizar_usuario, name='actualizar_usuario'),
    path('user/<int:pk>/delete/', views.eliminar_usuario, name='eliminar_usuario'),
    path('get_localidades/', views.get_localidades, name='get_localidades'),

    path('user/new/', views.crear_usuario, name='crear_usuario'),

    # familias

    path('families/', views.listar_familias, name='listar_familias'),
    path('family/new/', views.crear_familia, name='crear_familia'),
    path('families/<int:pk>/edit/', views.editar_familia, name='editar_familia'),
    path('families/<int:pk>/delete/', views.eliminar_familia, name='eliminar_familia'),

    # usuarios familias

    path('user/family/', views.listar_usuario_familia, name='listar_usuario_familia'),
    path('user/family/new/', views.crear_usuario_familia, name='crear_usuario_familia'),
    path('user/family/<int:pk>/edit/', views.editar_usuario_familia, name='editar_usuario_familia'),
    path('user/family/<int:pk>/delete/', views.eliminar_usuario_familia, name='eliminar_usuario_familia'),


    # eventos

    path('events/', views.listar_eventos, name='listar_eventos'),
    path('event/new/', views.crear_evento, name='crear_evento'),
    path('event/<int:pk>/edit/', views.editar_evento, name='editar_evento'),
    path('event/<int:pk>/delete/', views.eliminar_evento, name='eliminar_evento'),

    # usuarios eventos

    path('users/events/', views.listar_usuarios_eventos, name='listar_usuarios_eventos'),
    path('user/events/new/', views.crear_usuario_evento, name='crear_usuario_evento'),
    path('user/events/<int:pk>/edit/', views.editar_usuario_evento, name='editar_usuario_evento'),
    path('user/events/<int:pk>/delete/', views.eliminar_usuario_evento, name='eliminar_usuario_evento'),
    path('events/<int:evento_id>/list/', views.listar_usuarios_por_evento, name='listar_usuarios_por_evento'),
    path('events/<int:evento_id>/registrar_usuario/', views.registrar_usuario_a_evento, name='registrar_usuario_a_evento'),
    path('assistance/user/<int:usuario_id>/', views.listar_asistencias_usuario, name='listar_asistencias_usuario'),

    # login

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),

    # otras rutas

    path('', views.index, name='index'), 
    path('history', views.historia, name='historia'), 
    path('mission/Vision ', views.misionVision, name='misionVision'), 
    path('events/schedule', views.cronograma_eventos, name='cronograma_eventos'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])