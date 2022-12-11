from django.urls import path
from django.views.generic.base import TemplateView
from .views.billing import views_billing
from .views.client import views_client

urlpatterns = [
    path('', TemplateView.as_view(template_name='billing.html'), name='billing'),
    path('factura', views_billing.bill_new, name='factura'),
    path('registro_ventas', views_billing.registro_ventas, name='registro_ventas'),
    path('cuenta_final', views_billing.cuenta_final, name='cuenta_final'),
    path('cliente', views_client.client_new, name='cliente'),
]