from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new), # form을 보여준다.
    path('create/', views.create),
    # Read
    # 경로가 지정되있지 않으면 연결해준다.
    path('', views.index),
    # 지정된 위치에 들어오는 숫자를 todo_id라고 한다.
    path('<int:todo_id>/', views.detail),
    # Update
    path('<int:todo_id>/edit/', views.edit),
    path('<int:todo_id>/update/', views.update),
    # Delete
    path('<int:todo_id>/delete/', views.delete),
]