from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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