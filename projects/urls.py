# projects/urls.py
from django.urls import path
from . import views

app_name = 'projects' # Пространство имен для URL

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),
]