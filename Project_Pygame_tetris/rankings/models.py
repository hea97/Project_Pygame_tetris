from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    score = models.IntegerField()

    def __str__(self):
        return self.username