from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Hackers(models.Model):
    name = models.CharField(max_length=1000)
    challenges_solved = models.IntegerField()
    vote = models.BigIntegerField(default=0)

    expertise_level = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])

    # Expert skills
    cpp = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    python = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    java = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    ds = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    algorithm = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])

