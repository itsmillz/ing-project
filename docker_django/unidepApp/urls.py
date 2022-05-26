# from django.urls import path
from unidepApp import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_propiedad, name='agregar'),
    path('<int:value>/', views.filtro_universidad, name='filtro-universidad'),
    path('<int:value2>/', views.filtro_precio, name='precio-arriendo'),
    path('<int:value3>/', views.filtro_dormitorios, name='dormitorios-arriendo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)