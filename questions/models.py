from django.db import models

class Questions(models.Model):
    question = models.CharField(max_length=255)
    answers = models.ManyToManyField("questions.Answers", verbose_name="answers", related_name="answers")

    def __str__(self):
        return self.name

class Answers(models.Model):
    answer = models.CharField(max_length=255)
    question = models.ManyToManyField("questions.Questions", verbose_name="question", related_name="question1")
    voters = models.ManyToManyField("users.User", verbose_name="voters")

