from rest_framework import generics
from django.http import JsonResponse

from .serializers import BoardSerializer, CardSerializer, TaskListSerializer, BoardUserRelationshipSerializer, BoardDetailSerializer, TaskListDetailSerializer
from .models import Board, TaskList, Card, BoardUserRelationship

class RetriveBoard(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer


class ListBoard(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

#
class ListTaskList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = TaskList.objects.filter(board_id = self.kwargs["pk"])
        return queryset
    serializer_class = TaskListSerializer


class RetriveTaskList(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = TaskList.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = TaskListDetailSerializer


class ListCard(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Card.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = CardSerializer


class RetriveCard(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Card.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = CardSerializer