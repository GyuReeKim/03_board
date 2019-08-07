from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new), # form을 보여준다.
    path('create/', views.create),
    # Read
    path('', views.index),
]