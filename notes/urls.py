from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('edit/<int:note_id>/', views.edit, name='edit'),
    path('delete/<int:note_id>/', views.delete, name='delete'),
    path('view/<int:note_id>/', views.view, name='view'),
]