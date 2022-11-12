# models.py
from django.db import models
from uuid import uuid4


class Question(models.Model):
    id = models.UUIDField(primary_key=True,
                          unique=True, default=uuid4)
    name = models.CharField(null=False, max_length=64, default='new')
    numInputs = models.IntegerField(null=True)
    createdAt = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        db_table = "questions"

    def __str__(self):
        return self.name
