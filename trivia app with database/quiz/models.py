from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)





class Question(models.Model):
    description = models.CharField(max_length=300)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.description)


class Choices(models.Model):
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.choice_text)


class QuizHistory(models.Model):
    user_name = models.CharField(max_length=100)
    marks = models.FloatField()
