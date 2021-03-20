from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
# Create your views here.

@api_view(['POST'])
def email_verificacion_correo(request):
    
    to = request.data.get('to', None)
    url = request.data.get('url', None)
    
    email_body = """\
    <html>
      <head></head>
      <body>
        <p style="color: #424242;">Para activar su cuenta, ingrese al siguiente enlace:</p>
        <a href="%s">%s</a><br>
        <p style="color: #424242; font-weight:bold;">Talento Humano Personal Paraguay</p>
      </body>
    </html>
    """ % (url, url)

    email = EmailMessage('Personal CV - Verificación de correo electrónico', email_body, to=[to])
    email.content_subtype = "html" # this is the crucial part 
    email.send()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def email_postulacion(request):
    
    to = request.data.get('to', None)
    nombre = request.data.get('nombre', None)

    email_body = """\
    <html>
      <head></head>
      <body>
        <p style="color: #424242;">Hola, <b>%s</b>.</p>
        <p style="color: #424242;">Recibimos tu cv con éxito, Personal agradece tu postulación. Analizaremos los datos y estaremos en contacto cuando surjan vacancias acorde a tu perfil profesional.</p>
        <p style="color: #424242;">Un saludo.</p>
        <p style="color: #424242; font-weight:bold;">Talento Humano Personal Paraguay</p>
      </body>
    </html>
    """ % (nombre)

    email = EmailMessage('Personal CV - Postulación a oportunidad laboral', email_body, to=[to])
    email.content_subtype = "html" # this is the crucial part 
    email.send()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def email_restablecer_clave(request):
    
    to = request.data.get('to', None)
    url = request.data.get('url', None)
    
    email_body = """\
    <html>
      <head></head>
      <body>
        <p style="color: #424242;">Para restablecer su contraseña, ingrese al siguiente enlace:</p>
        <a href="%s">%s</a><br>
        <p style="color: #424242; font-weight:bold;">Talento Humano Personal Paraguay</p>
      </body>
    </html>
    """ % (url, url)

    email = EmailMessage('Personal CV - Restablecer contraseña', email_body, to=[to])
    email.content_subtype = "html" # this is the crucial part 
    email.send()
    return Response(status=status.HTTP_200_OK)