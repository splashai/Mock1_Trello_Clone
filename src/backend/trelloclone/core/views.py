from rest_framework import generics

from .serializers import BoardSerializer, CardSerializer, TaskListSerializer, BoardUserRelationshipSerializer
from .models import Board, TaskList, Card, BoardUserRelationship

class ListBoard(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class ListBoard(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class ListTaskList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = TaskList.objects.filter(board_id = self.kwargs["pk"])
        return queryset
    serializer_class = TaskListSerializer


class ListTaskList(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = TaskList.objects.filter(board_id = self.kwargs["pk"])
        return queryset
    serializer_class = TaskListSerializer


class ListCard(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = TaskList.objects.filter(board_id = self.kwargs["pkb"])
        return queryset
    serializer_class = CardSerializer