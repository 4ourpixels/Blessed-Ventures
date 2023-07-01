from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_stone, name='view_stone'),
    path('add/', views.add, name='add'),
]
