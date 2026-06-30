from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(primary_key=True, max_length=100, default='')
    name = models.CharField(max_length=150, default='')
    email = models.EmailField(default='')
    age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.nickname}. Email: {self.name}'