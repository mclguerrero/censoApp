from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import CustomUserCreationForm, CustomAuthenticationForm, EventoForm, UsuarioForm
from django.contrib.auth.models import Group, User
from django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import default_storage

def crear_usuario(request):    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        # Imprimir los datos que se están intentando guardar
        print("Datos del formulario:", request.POST)

        if form.is_valid():
            try:
                usuario = form.save(commit=False)
                n_documento = form.cleaned_data['n_documento']
                
                # Imprimir los datos que se guardarán
                print("Datos validados para guardar:", usuario)
                print("Número de documento:", n_documento)
                
                user, created = User.objects.get_or_create(
                    username=n_documento,
                    defaults={
                        'first_name': form.cleaned_data['nombres'],
                        'last_name': form.cleaned_data['apellidos']
                    }
                )
                
                if created:
                    user.set_password(n_documento)
                    user.save()
                    
                    try:
                        group = Group.objects.get(name='Usuario')
                        user.groups.add(group)
                        messages.success(request, 'El usuario se ha creado con éxito.')
                    except Group.DoesNotExist:
                        messages.warning(request, 'Error: El grupo "Usuario" no está configurado en el sistema.')
                else:
                    messages.warning(request, 'El usuario con este número de documento ya existe en el sistema.')

                usuario.user = user
                usuario.save()

                form = UsuarioForm()
            
            except Exception as e:
                messages.warning(request, f'Ocurrió un error inesperado al crear el usuario: {str(e)}')
                for field, errors in form.errors.items():
                    for error in errors:
                        print(f'Error en {field}: {error}')
        else:
            messages.warning(request, 'Hay errores en el formulario. Por favor corrige los campos indicados.')
            print("Errores del formulario:", form.errors)  # Imprimir los errores si el formulario no es válido
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/crear.html', {'form': form})


# eventos

def listar_eventos(request):
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos/listar.html', context)

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, f'El Evento se ha creado con éxito.')
            form = EventoForm()  
    else:
        form = EventoForm()
    
    context = {'form': form}
    return render(request, 'eventos/crear.html', context)

def actualizar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento) 
        if form.is_valid():
            form.save()
            messages.success(request, f'El Evento se ha editado con éxito.')
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    
    context = {'form': form}
    return render(request, 'eventos/actualizar.html', context)

def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)

    if evento.imagen:
        if default_storage.exists(evento.imagen.path):
            default_storage.delete(evento.imagen.path)
    
    evento.delete()
    messages.success(request, f'El Evento se ha eliminado con éxito.')

    return redirect('listar_eventos')

# registrarse

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()  
                group = Group.objects.get(name='Usuario') 
                user.groups.add(group) 
                return redirect('signin')
            except IntegrityError:
                form.add_error(None, "El nombre de usuario ya existe.")
        else:
            return render(request, 'login/signup.html', {"form": form})

    else:
        form = CustomUserCreationForm()
    return render(request, 'login/signup.html', {"form": form})
        
# iniciar sesion

def signin(request):
    if request.method == 'GET':
        return render(request, 'login/signin.html', {"formAuth": CustomAuthenticationForm()})
    else:
        # Autenticar usuario
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/signin.html', {"formAuth": CustomAuthenticationForm(), "error": "Usuario o contraseña incorrecta."})
        
        login(request, user)
        
        # Redirigir según grupo
        if user.groups.filter(name='Admin').exists():
            return redirect('listar_eventos')  
        elif user.groups.filter(name='Usuario').exists():
            return redirect('listar_eventos')  
        else:
            return redirect('index')  

# cerrar sesion

@login_required
def signout(request):
    logout(request)
    return redirect('index')

# -----------------

def index(request):
    eventos = Evento.objects.filter(es_favorito=True)
    return render(request, 'bases/landing/index.html', {'eventos': eventos})

def historia(request):
    return render(request, 'bases/landing/otros/historia.html')

def misionVision(request):
    return render(request, 'bases/landing/otros/misionVision.html')

def cronograma_eventos(request):
    eventos = Evento.objects.filter(es_favorito=True).order_by('-fecha_inicio') 
    return render(request, 'bases/landing/otros/cronograma.html', {'eventos': eventos})

