from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_stone, name='view_stone'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('<int:id>', views.view_project, name='view_project'),
    path('new_project/', views.new_project, name='new_project'),
    path('edit_project/<int:id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:id>/', views.delete_project, name='delete_project'),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('mazeras/', views.mazeras, name="mazeras"),
    path('thetap/', views.thetap, name="thetap"),
]
