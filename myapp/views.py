from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse

from .forms import CompraModelForm
from .models import ComprarArticulo

#Create your views here.
#Vistas basadas en clases
#Para proteger y decorar clases, de este modo hay que loguearse para poder hacer operaciones de borrar, crear, editar
class StaffRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class MyAppTemplateView(TemplateView):
	template_name = "home.html"

	#Obtiene el contexto de dicha plantilla (objetos, query, etc..)
	def get_context_data(self, *args, **kwargs):
		context = super(MyAppTemplateView, self).get_context_data(*args, **kwargs)
		context["titulo"] = "Eat the rainbow"
		return context
#Create
class Create(CreateView):
	#model = ComprarArticulo
	#fields = ["nombre", "tipo_de_comida"]
	template_name = "form.html"
	form_class = CompraModelForm

	def get_success_url(self):
		return reverse("lista")
#Update
class Update(StaffRequiredMixin,UpdateView):
	model = ComprarArticulo
	# fields = []
	form_class = CompraModelForm
	template_name = "myapp/comprararticulo_update.html"
#Delete
class Delete(DeleteView):
	model = ComprarArticulo

	def get_success_url(self):
		return reverse("list")		

#Details
class Detail(DetailView):
	model = ComprarArticulo

#Objects list
class List(ListView):
	model = ComprarArticulo
	#Queryset con todos lo objectos de este modelo guardados en la BD
	def get_context_data(self, *args, **kwargs):
		context = super(List, self).get_context_data(*args, **kwargs)
		context['query'] = ComprarArticulo.objects.all()
		return context

#Para la autenticación de usuarios
def register(request):
	# Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('home/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})

def login(request):
	 # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('home/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})
	
def logout(request):
	# Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('home')

def welcome(request):
	template = "users/welcome.html" 
	return render(request,template, {})	

#Para las vistas basadas en funciones
def home(request):
	template = "home.html"
	context = {}
	return render(request, template, context)

def lista(request):
    template = "lista.html"
    queryset = ComprarArticulo.objects.all()
    context = {
        "queryset": queryset
    }
    return render(request, template, context)


def detail(request, pk=None):
	producto = get_object_or_404(ComprarArticulo, pk=pk)
	template = "detail.html"
	context = {
		"titulo": "SOBRE EL PRODUCTO",
		"objeto": producto
	}

	return render(request, template, context)


@login_required (login_url='/admin/')
def create(request):
    form = CompraModelForm(request.POST or None)
    template = "form.html"
    context = {
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        #codigo
        instance.save()
        return redirect(instance) 
    return render(request, template, context)


@login_required(login_url='/admin/')
def update(request, pk=None):
	producto = get_object_or_404(ComprarArticulo, pk=pk)
	form = CompraModelForm(request.POST or None, instance=producto)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	template = "update.html"
	if request.method == 'POST':
		producto.save()
		return HttpResponseRedirect("/lista/")
	context = {
		"objeto": producto,
		"form": form,
		}
	return render(request, template, context)


@login_required(login_url='/admin/')
def delete(request, pk):
	producto = get_object_or_404(ComprarArticulo, pk=pk)
	template = "delete.html"
	
	if request.method == 'POST':
		producto.delete()
		return HttpResponseRedirect("/lista/")
	
	context = {
		"objeto": producto
		}
	return render(request, template, context)