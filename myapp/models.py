from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    study_hours = models.FloatField()
    attendance = models.FloatField()
    previous_marks = models.FloatField()
    sleep_hours = models.FloatField()
    predicted_marks = models.FloatField(null=True, blank=True)
    result = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name