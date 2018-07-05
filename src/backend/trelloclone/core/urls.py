from django.urls import path

from . import views

urlpatterns = [
    path('v1/boards/', views.ListBoard.as_view()),
]