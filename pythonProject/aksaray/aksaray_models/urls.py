from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('menu/', views.menu, name='menu')
]