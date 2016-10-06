from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^registration-added/', views.registration_added, name='registration_added'),
    url(r'^$', views.add_registration, name='add_registration'),        
]