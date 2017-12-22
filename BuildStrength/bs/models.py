from django.db import models
from django.contrib.auth.models import User


DAYS = (
    ("A", "Dzień A"),
    ("B", "Dzień B"),
)


class Lifts(models.Model):
    user = models.ForeignKey(User)
    deadlift = models.FloatField(default="20")
    oh_press = models.FloatField(default="20")
    barbell_row = models.FloatField(default="20")
    bench_press = models.FloatField(default="20")
    squat = models.FloatField(default="20")
    pull_ups = models.IntegerField(default="max")
    last_training = models.CharField(max_length=1, choices=DAYS)
    training_count = models.IntegerField(default="0")


class HistoryA(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    deadlift = models.FloatField(default="0")
    oh_press = models.FloatField(default="0")
    barbell_row = models.FloatField(default="0")


class HistoryB(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    bench_press = models.FloatField(default="0")
    squat = models.FloatField(default="0")
    pull_ups = models.IntegerField(default="0")


class Maxes(models.Model):
    user = models.ForeignKey(User)
    deadlift = models.FloatField(default="0")
    oh_press = models.FloatField(default="0")
    barbell_row = models.FloatField(default="0")
    bench_press = models.FloatField(default="0")
    squat = models.FloatField(default="0")
    pull_ups = models.IntegerField(default="0")
