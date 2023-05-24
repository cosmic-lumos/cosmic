from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'post'
urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('',views.post_list, name='post_list'),
]