from rest_framework import serializers

from .models import Board, TaskList, Card, BoardUserRelationship


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many = True, required =False)
    class Meta:
        model = TaskList
        fields = '__all__'


class BoardUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUserRelationship
        fields = '__all__'
