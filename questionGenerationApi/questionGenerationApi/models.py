# models.py
from django.db import models
from uuid import uuid4


class Question(models.Model):
    id = models.UUIDField(primary_key=True,
                          unique=True, default=uuid4)
    name = models.CharField(null=False, max_length=64, default='new')
    questionText = models.TextField(
        null=False, default='unset', help_text='Full question text')
    answer = models.TextField(
        null=False, default='unset', help_text='Full answer text')
    difficulty = models.IntegerField(null=True)
    numInputs = models.IntegerField(null=True)
    createdAt = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        db_table = "questions"

    def __str__(self):
        return f'[Name: {self.name}, Question: {self.questionText}, Answer: {self.answer}]'
