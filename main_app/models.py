from django.db import models
from django.urls import reverse

# Create your models here.

class Visitor(models.Model):
  name = models.CharField(max_length=50)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('visitors_detail', kwargs={'pk': self.id})

class Trip(models.Model):
  city = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  duration = models.IntegerField()
  visitors = models.ManyToManyField(Visitor)

  def __str__(self):
    return self.city
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'trip_id': self.id})

class Sight(models.Model):
  date = models.DateField()
  name = models.CharField(max_length=100)

  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

  # def __str__(self):
  #   # Nice method for obtaining the friendly value of a Field.choice
  #   return f"{self.get_name_display()} on {self.date}"
  
  