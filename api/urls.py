from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import email_verificacion_correo, email_restablecer_clave, email_postulacion

urls = [
    path('verificar-correo', email_verificacion_correo),
    path('postulacion-correo', email_postulacion),
    path('restablecer-clave-correo', email_restablecer_clave)
]

urlpatterns = format_suffix_patterns(urls)
