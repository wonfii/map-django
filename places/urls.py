from django.urls import path
from . import views

urlpatterns = [
    path('', views.ua_map),
    path('create/', views.create),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id>/', views.edit),
    path('add/', views.add),
]