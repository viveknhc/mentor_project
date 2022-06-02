from distutils.command.upload import upload
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Catagory(models.Model):
    catagory = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory

class Course(models.Model):
    catagory_id = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    courseImage = models.ImageField(upload_to="images") 
    description = models.CharField(max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.course_name

class Trainer(models.Model):
    catagory_id = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    trainer_img = models.ImageField(upload_to="trainer")
    trainer_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    person = models.CharField(max_length=50)
    post = models.CharField(max_length=100)
    quote = models.CharField(max_length=1000)
    person_img = models.ImageField(upload_to="testimonial")

    def __str__(self):
        return self.person

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name