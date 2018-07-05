from rest_framework import generics

from .serializers import BoardSerializer
from .models import Board, TaskList, Card, BoardUserRelationship

class ListBoard(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer