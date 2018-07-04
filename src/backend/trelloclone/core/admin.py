from django.contrib import admin
from .models import Board, TaskList, Card, BoardUserRelationship

# Register your models here.
admin.site.register(Board)
admin.site.register(TaskList)
admin.site.register(Card)
admin.site.register(BoardUserRelationship)