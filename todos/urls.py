from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new), # form을 보여준다.
    path('create/', views.create),
]