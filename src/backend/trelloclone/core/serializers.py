from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

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


class TaskListDetailSerializer(serializers.ModelSerializer):
    card_set = CardSerializer(many = True, required =False)
    class Meta:
        model = TaskList
        fields = '__all__'

    def update(self, instance, validated_data):
        # Update the  instance
        instance.name = validated_data['name']
        instance.position = validated_data['position']
        instance.is_archived = validated_data['is_archived']
        instance.save()
        return instance


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class BoardDetailSerializer(serializers.ModelSerializer):
    tasklist_set = TaskListDetailSerializer(many=True, required=False)
    class Meta:
        model = Board
        fields = '__all__'

    extra_kwargs = {
        'id': {
            'read_only': False,
            'required': True
        }
    }

    def update(self, instance, validated_data):
        # Update the  instance
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.is_private = validated_data['is_private']
        instance.is_archived = validated_data['is_archived']
        instance.created_by = validated_data['created_by']
        instance.save()
        return instance


class BoardUserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUserRelationship
        fields = '__all__'
