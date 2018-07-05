from django.urls import path

from . import views

urlpatterns = [
    path('v1/boards/', views.ListBoard.as_view()),
    path('v1/boards/<int:pk>/tasklists/', views.ListTaskList.as_view()),
    path('v1/boards/<int:pkb>/tasklists/<int:pkc>/cards/', views.ListCard.as_view()),
]