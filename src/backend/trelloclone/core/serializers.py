from rest_framework import serializers

from .models import Board, TaskList, Card, BoardUserRelationship


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    card_set = CardSerializer(many = True, required =False)
    class Meta:
        model = TaskList
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    tasklist_set = TaskListSerializer(many=True, required=False)
    class Meta:
        model = Board
        fields = '__all__'


class BoardUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUserRelationship
        fields = '__all__'
