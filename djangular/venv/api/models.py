from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)
    year = models.IntegerField()
# No olvidar hacer:   $ python manage.py makemigrations | python manage.py migrate
