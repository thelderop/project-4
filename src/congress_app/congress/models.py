from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)

class Senator(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    voting_record = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Senate_Bill(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField(default='Healthcare is not as expensive as the corporate media might have you believe.')
    senator = models.ManyToManyField(Senator)