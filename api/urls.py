from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='onrec-home'),
    path('about/', views.about, name='onrec-about'),
]