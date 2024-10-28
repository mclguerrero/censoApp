# main/context_processors.py
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

def is_user_admin(user):
    return user.groups.filter(name='Admin').exists()

# Decorador que utiliza la función de verificación
admin_required = user_passes_test(is_user_admin)

def is_admin(request):
    if request.user.is_authenticated:
        is_admin = is_user_admin(request.user)
    else:
        is_admin = False
    return {'is_admin': is_admin}
