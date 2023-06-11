from django.db import models


class CreateTest(models.Model):
    login = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.login


class IqTest(models.Model):
    login = models.ForeignKey(CreateTest, on_delete=models.CASCADE)
    score = models.IntegerField()
    finish_time = models.DateTimeField(auto_now_add=True)


class EqTest(models.Model):
    login = models.ForeignKey(CreateTest, on_delete=models.CASCADE)
    score = models.IntegerField()
    finish_time = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=5)
