
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('dbmsproject/', views.dbmsproject, name='blog-dbmsproject'),
    path('', views.download_file, name='download'),



]