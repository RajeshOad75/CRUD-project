from django.db import models

# Create your models here.


class Student(models.Model):
    image = models.ImageField(default='default.jpg', upload_to="loginApp/")
    name = models.TextField(max_length=200),
    address = models.TextField(max_length=200),
    email = models.TextField(max_length=200),
    tel_number = models.IntegerField(max_length=12),
    gender = models.TextField(max_length=200),
    remarks = models.TextField(max_length=200)

    def _str_(self):
        return self.name
