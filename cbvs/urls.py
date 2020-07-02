from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView


from myapp.views import (
    MyAppTemplateView,
    Create,
    Detail,
    List,
    Update,
    Delete,
    home,
	create,
	lista,
	detail,
	update,
    delete,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Por clases bases
    url(r'^home/$', MyAppTemplateView.as_view(), name='home'),
    url(r'^create/$', Create.as_view(), name='create'),
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
]