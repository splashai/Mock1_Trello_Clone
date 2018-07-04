from django.db import models
from django.contrib.auth.models import User


ROLE_CHOICES = (
    ("owner", "Owner"),
    ("contributor", "Contributor"),
)

class Board(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    is_private = models.BooleanField()
    is_archived = models.BooleanField()

    def __str__(self):
        return self.name


class TaskList(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    position = models.IntegerField()
    is_archived = models.BooleanField()

    def __str__(self):
        return self.name


class Card(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title


class BoardUserRelationship(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50,choices=ROLE_CHOICES, default = 'contributor')

    def __str__(self):
        return '{} - {} - {}'.format(self.board, self.role, self.user)
