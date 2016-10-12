from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^registration-added/', views.registration_added, name='registration_added'),
    url(r'^$', views.add_registration, name='add_registration'),
    url(r'^attended/(?P<key>[a-z0-9]{30})$', views.invitee_attended, name='attended'),
]