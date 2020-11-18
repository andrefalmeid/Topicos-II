from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import *
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('restaurante', views.Restaurante_list, name='restaurante'),
    path('produto', views.Produto_list, name='produto'),
    path('restaurante_edit/<int:pk>', views.Restaurante_edit, name='restaurante_edit'),
    path('restaurante_delete/<int:pk>', views.Restaurante_delete, name='restaurante_delete'),
    path('produto_edit/<int:pk>', views.Produto_edit, name='produto_edit'),
    path('produto_delete/<int:pk>', views.Produto_delete, name='produto_delete'),
    path('restaurante_print_pdf', views.Restaurante_Print_pdf, name='restaurante_print_pdf'),
    path('produto_print_pdf', views.Produto_Print_pdf, name='produto_print_pdf'),

]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)