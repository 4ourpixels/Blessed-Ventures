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

    path('<int:id>', views.view_uncut_mazeras, name='view_uncut_mazeras'),
    path('add_uncut_mazeras/', views.add_uncut_mazeras, name='add_uncut_mazeras'),
    path('edit_uncut_mazeras/<int:id>/',
         views.edit_uncut_mazeras, name='edit_uncut_mazeras'),
    path('delete_uncut_mazeras/<int:id>/',
         views.delete_uncut_mazeras, name='delete_uncut_mazeras'),

    path('<int:id>', views.view_cut_mazeras, name='view_cut_mazeras'),
    path('add_cut_mazeras/', views.add_cut_mazeras, name='add_cut_mazeras'),
    path('edit_cut_mazeras/<int:id>/',
         views.edit_cut_mazeras, name='edit_cut_mazeras'),
    path('delete_cut_mazeras/<int:id>/',
         views.delete_cut_mazeras, name='delete_cut_mazeras'),
]
