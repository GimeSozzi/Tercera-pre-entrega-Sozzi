from django.urls import path
from app_proyectos import views


app_name = 'app_proyectos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-proyecto/', views.crear_proyecto, name='crear-proyecto'),
    path('buscar-proyecto/', views.buscar_proyecto, name='buscar-proyecto'),
]
