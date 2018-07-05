from django.urls import path

from . import views

urlpatterns = [
    path('v1/boards/', views.ListBoard.as_view()),
    path('v1/boards/<int:pk>/', views.RetriveBoard.as_view()),
    path('v1/boards/<int:pk>/tasklists/', views.ListTaskList.as_view()),
    path('v1/boards/<int:pkb>/tasklists/<int:pk>/', views.RetriveTaskList.as_view()),
    path('v1/boards/<int:pkb>/tasklists/<int:pkc>/cards/<int:pk>/', views.RetriveCard.as_view()),
]