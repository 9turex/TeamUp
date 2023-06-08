from django.db import models
from django.utils.crypto import get_random_string


class CreateTest(models.Model):

    login = models.CharField(max_length=10)

    def __init__(self):
        self.login = get_random_string(length=10)
        while CreateTest.objects.filter(login=self.login).exists():
            self.login = get_random_string(length=10)


a = CreateTest()
b = CreateTest

print(a.login)
print(b.login)
