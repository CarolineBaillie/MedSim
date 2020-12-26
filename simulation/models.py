from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Simulation(models.Model):
    user = models.CharField(max_length=150)
    title = models.CharField(max_length=47)
    desc = models.TextField()
    difficulty = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    race = models.CharField(max_length=150)
    birth = models.CharField(max_length=150)
    weight = models.CharField(max_length=150)
    height = models.CharField(max_length=150)
    sexuallyActive = models.CharField(max_length=150)
    medications = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    illnesses = models.TextField(blank=True, null=True)
    symptoms = models.TextField()
    notes = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=150, blank=True, null=True)
    diagnosis = models.CharField(max_length=150)
    test1 = models.CharField(max_length=150, blank=True, null=True)
    desc1 = models.TextField(blank=True, null=True)
    test1Res = models.CharField(max_length=150, blank=True, null=True)
    test2 = models.CharField(max_length=150, blank=True, null=True)
    desc2 = models.TextField(blank=True, null=True)
    test2Res = models.CharField(max_length=150, blank=True, null=True)
    test3 = models.CharField(max_length=150, blank=True, null=True)
    desc3 = models.TextField(blank=True, null=True)
    test3Res = models.CharField(max_length=150, blank=True, null=True)
    test4 = models.CharField(max_length=150, blank=True, null=True)
    desc4 = models.TextField(blank=True, null=True)
    test4Res = models.CharField(max_length=150, blank=True, null=True)
    test5 = models.CharField(max_length=150, blank=True, null=True)
    desc5 = models.TextField(blank=True, null=True)
    test5Res = models.CharField(max_length=150, blank=True, null=True)
    test6 = models.CharField(max_length=150, blank=True, null=True)
    desc6 = models.TextField(blank=True, null=True)
    test6Res = models.CharField(max_length=150, blank=True, null=True)
    tNum = models.IntegerField()
    quest1 = models.TextField(blank=True, null=True)
    resp1 = models.TextField(blank=True, null=True)
    quest2 = models.TextField(blank=True, null=True)
    resp2 = models.TextField(blank=True, null=True)
    quest3 = models.TextField(blank=True, null=True)
    resp3 = models.TextField(blank=True, null=True)
    quest4 = models.TextField(blank=True, null=True)
    resp4 = models.TextField(blank=True, null=True)
    quest5 = models.TextField(blank=True, null=True)
    resp5 = models.TextField(blank=True, null=True)
    quest6 = models.TextField(blank=True, null=True)
    resp6 = models.TextField(blank=True, null=True)
    qNum = models.IntegerField()
    hint1 = models.TextField(blank=True, null=True)
    hint2 = models.TextField(blank=True, null=True)
    hint3 = models.TextField(blank=True, null=True)
    hint4 = models.TextField(blank=True, null=True)

class Game(models.Model):
    user = models.CharField(max_length=150)
    simID = models.PositiveIntegerField()
    hints = models.TextField(blank=True, null=True)
    questions = models.TextField(blank=True, null=True)
    tests = models.TextField(blank=True, null=True)
    diagnosis = models.CharField(max_length=150, blank=True, null=True)
    score = models.IntegerField(default=50)
    isFinished = models.BooleanField(default=False)
    isDiagnosed = models.BooleanField(default=False)
    isStarred = models.BooleanField(default=False)

class Complete(models.Model):
    simID = models.PositiveIntegerField()
    title = models.CharField(max_length=47)
    desc = models.TextField()
    score = models.IntegerField(default=50)
    correctDiag = models.BooleanField(default=False)