from django.db import models

# Command for making DB from models
# python manage.py makemigrations -> store temporarily in a file
# python manage.py migrate -< store models in form of DB table in admin DB

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
