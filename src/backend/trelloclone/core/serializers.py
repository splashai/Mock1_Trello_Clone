from rest_framework import serializers

from .models import Board, TaskList, Card, BoardUserRelationship


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    pass


class BoardUserRelationshipSerializer(serializers.ModelSerializer):
    pass
