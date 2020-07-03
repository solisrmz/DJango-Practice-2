from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

from myapp.views import (
    MyAppTemplateView,
    Create,
    Detail,
    List,
    Update,
    Delete,
    home,
	create,
    CreateNota,
	lista,
	detail,
	update,
    delete,
    register,
    welcome,
    login,
    logout,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Por clases bases
    url(r'^home/$', MyAppTemplateView.as_view(), name='home'),
    url(r'^create/$', Create.as_view(), name='create'),
    url(r'^create-nota/$', CreateNota, name='create-nota'),
    url(r'^detail/(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    url(r'^lista/$', List.as_view(), name='lista'),
    url(r'^edit/(?P<pk>\d+)/$', Update.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', Delete.as_view(), name='delete'),

    #Por funciones
    url(r'^create/$', create, name='create'),
    url(r'^lista/$', lista, name='lista'),
    url(r'^detail/(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^detail/(?P<pk>\d+)/edit/$', update, name='update'),
    url(r'^detail/(?P<pk>\d+)/delete/$', delete, name='delete'),

    #Para la autenticación
    url('register', register, name="register"),
    url('login', login, name="login"),
    url('logout', logout, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)