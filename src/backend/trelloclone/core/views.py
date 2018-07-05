from rest_framework import generics

from .serializers import BoardSerializer, CardSerializer, TaskListSerializer, BoardUserRelationshipSerializer, BoardDetailSerializer
from .models import Board, TaskList, Card, BoardUserRelationship

class ListBoard(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class RetriveBoard(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer

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
    serializer_class = TaskListSerializer


class ListCard(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = TaskList.objects.filter(board_id = self.kwargs["pk"])
        return queryset
    serializer_class = CardSerializer