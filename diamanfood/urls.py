from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', include('cliente.urls'),name='cliente'),
    path('restaurantes/', include('restaurantes.urls'),name='restaurantes'),
]

