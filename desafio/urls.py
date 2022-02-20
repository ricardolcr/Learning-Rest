from django.urls import path
from desafio.ip import views

urlpatterns = [
    path('', views.home, name='home'),
    path('previous/', views.previous, name='previous'),
]