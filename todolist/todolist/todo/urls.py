from django.conf.urls import url
from django.views.generic import ListView, DetailView
from django.contrib.auth import views as auth_views
from .models import Todo
from . import views
from .views import delete, edit
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup' ),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^$',views.index, name='index'),
    url(r'^details/(?P<pk>\w{0,50})/$', views.details, name='details'),
    # url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details'),
    url(r'^add/', views.add, name='add'),
    url(r'^details/(?P<pk>\w{0,50})/delete/$', views.delete.as_view(), name='delete'),
    url(r'^details/(?P<pk>\w{0,50})/edit/$', edit.as_view(), name='edit'),
    
]