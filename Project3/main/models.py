from django.db import models


from django.contrib.postgres.fields import ArrayField
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    improve_answer = ArrayField(models.CharField(max_length=30))

    preexisting_conditions = ArrayField(models.CharField(max_length=30))

    dietary_restrictions = ArrayField(models.CharField(max_length=30))

    workouts = ArrayField(models.CharField(max_length=30))

    workout_body_area = ArrayField(models.CharField(max_length=30))

    workout_days_per_week = models.IntegerField()






    streak_count = models.IntegerField();

    