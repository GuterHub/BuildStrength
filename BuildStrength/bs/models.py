from django.db import models
from django.contrib.auth.models import User


class Lifts(models.Model):
    user = models.ForeignKey(User)
    deadlift = models.IntegerField(default="20")
    oh_press = models.IntegerField(default="20")
    barbell_row = models.IntegerField(default="20")
    bench_press = models.IntegerField(default="20")
    squat = models.IntegerField(default="20")
    pull_ups = models.IntegerField(default="max")
