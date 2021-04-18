from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns =  [
    path('', TaskView.as_view(), name = 'home'),
    path('task/<int:pk>/', DetailTaskView.as_view(), name = 'detail_task'),

    path('create_task/', CreateTaskView.as_view(), name = 'add_task'),
    path('update_task/<int:pk>/', UpdateTaskView.as_view(), name = 'update_task'),
    path('delete_task/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),


    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('register/', RegisterView.as_view(), name='register')

]