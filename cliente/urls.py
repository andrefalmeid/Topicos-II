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
    path('', views.home, name='home'),
    path('cliente', views.Cliente_list, name='cliente'),
    path('pedido', views.Pedido_list, name='pedido'),
    path('cliente_edit/<int:pk>', views.Cliente_edit, name='cliente_edit'),
    path('cliente_delete/<int:pk>', views.Cliente_delete, name='cliente_delete'),
    path('pedido_edit/<int:pk>', views.Pedido_edit, name='pedido_edit'),
    path('pedido_delete/<int:pk>', views.Pedido_delete, name='pedido_delete'),
    path('cliente_print_pdf', views.Cliente_Print_pdf, name='cliente_print_pdf'),
    path('pedido_print_pdf', views.Pedido_Print_pdf, name='pedido_print_pdf'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)