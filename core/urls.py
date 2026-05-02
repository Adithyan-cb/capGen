from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_page, name='generate_page'),
    path('results/', views.generate, name='results'),
]
