# urls

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

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