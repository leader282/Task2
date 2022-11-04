from django.db import models

# Create your models here.

class Food(models.Model):
    name=models.CharField(max_length=1000)
    price=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Restaurants(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(max_length=10000)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    ratings_num = models.IntegerField()
    avg_time = models.IntegerField()
    type = models.CharField(max_length=300)
    image_url = models.CharField(max_length=1000, null=True)
    menu = models.ManyToManyField(Food, related_name="menu")
    location = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.name