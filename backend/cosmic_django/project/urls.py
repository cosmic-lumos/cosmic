from django.urls import path
from project import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('new/', views.project_new, name='project_new'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/', views.project_delete, name='project_delete'),
]