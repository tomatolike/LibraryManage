from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/',views.login, name = 'login'),
    url(r'^main/',views.main, name = 'main'),
    url(r'^insertone/', views.insertone, name = 'insertone'),
    url(r'^insertfile/', views.insertfile, name = 'insertfile'),
    url(r'^search/',views.search, name = 'search'),
    url(r'^borrow/',views.borrow, name = 'borrow'),
    url(r'^borrowone/',views.borrowone, name = 'borrowone'),
    url(r'^return/', views.returnn, name = 'return'),
    url(r'^returnone/',views.returnone, name = 'returnone'),
    url(r'^card/',views.card, name = 'card'),
    url(r'^addcard/',views.addcard, name = 'addcard'),
    url(r'^deletecard/',views.deletecard, name = 'deletecard'),
    url(r'^logout/',views.logout,name = 'logout'),
]
