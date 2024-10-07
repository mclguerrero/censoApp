# urls

from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #select2

    path("select2/", include("django_select2.urls")),

    #usuarios

    path('user/new/', views.crear_usuario, name='crear_usuario'),
    path('users/', views.listar_usuarios, name='listar_usuarios'),
    path('user/<int:pk>/edit/', views.actualizar_usuario, name='actualizar_usuario'),
    path('user/<int:pk>/delete/', views.eliminar_usuario, name='eliminar_usuario'),
    path('get_localidades/', views.get_localidades, name='get_localidades'),

    path('user/new/', views.crear_usuario, name='crear_usuario'),

    # eventos

    path('events/', views.listar_eventos, name='listar_eventos'),
    path('event/new/', views.crear_evento, name='crear_evento'),
    path('event/<int:pk>/edit/', views.actualizar_evento, name='actualizar_evento'),
    path('event/<int:pk>/delete/', views.eliminar_evento, name='eliminar_evento'),


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