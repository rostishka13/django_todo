from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .import views

urlpatterns = [
    # path('',views.task_list),
    # path('task/<int:pk>', views.task_detail)

    path('', views.TaskList.as_view()),
    path('<int:pk>/', views.TaskDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('register', views.registration_view, name = 'register'),
    path('login',  obtain_auth_token, name = 'login')



    # path('', views.apiOverview, name = 'api-overview'),
    # path('task-list/', views.taskList, name = 'task-list'),
    # path('task-detail/<str:pk>/', views.taskDetail, name = 'task-detail' ),
    # path('task-create/', views.taskCreate, name = 'task-create'),
    # path('task-update/<str:pk>/', views.taskUpdate, name = 'task-update'),
    # path('task-delete/<str:pk>/', views.taskDelete, name = 'task-delete'),
]


