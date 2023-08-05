from django.urls import path
from ShowApp import views

from django.contrib.auth.views import LogoutView
from .views import FotoUpdate, ComentarioPagina

urlpatterns = [
   
    path('', views.home, name="Home"),
    path('art',views.art, name='Art'),
    path('showWork',views.artFormulario, name='ShowWork'),
    path('artReadFoto', views.artReadFotografia, name= 'ArtReadFoto' ),
    path('artDeleteFoto/<foto_name>', views.artDeleteFoto, name= 'ArtDeleteFoto'),
    path('artEditFoto/<int:pk>/', FotoUpdate.as_view(), name='ArtEditFoto'),
    path('expandObject/<foto_name>', views.expandObject, name='expandObject'),
    path('comentario_pagina/<int:pk>/', ComentarioPagina.as_view(), name='comentario'),
    path('team',views.team, name='Team'),
    path('workinprogress', views.workinprogress, name='WorkInProgress'),
    
  
      
    
]