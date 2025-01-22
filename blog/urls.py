from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('edit/', views.edit_post, name = 'edit_post')
]