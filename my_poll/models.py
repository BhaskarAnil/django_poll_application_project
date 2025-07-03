from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=200)
    date = models.DateTimeField('date')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
