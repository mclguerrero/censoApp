from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.api.v1.urls')),
    path('', include('main.urls')),
]
