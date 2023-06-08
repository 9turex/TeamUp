from django.db import models


class CreateTest(models.Model):
    login = models.CharField(max_length=10)


class IqTest(models.Model):
    login = models.ForeignKey(CreateTest, on_delete=models.CASCADE)
    score = models.IntegerField()
    finish_time = models.DateTimeField()


class EqTest(models.Model):
    login = models.ForeignKey(CreateTest, on_delete=models.CASCADE)
    score = models.IntegerField()
    finish_time = models.DateTimeField()
    answer = models.CharField(max_length=5)
