from django.db import models


class food_category(models.Model):
    name=models.CharField(max_length=254,unique=True)
    def __str__ (self):
        return self.name
class food(models.Model):
    name=models.CharField(max_length=254)
    category=models.ForeignKey(food_category,on_delete=models.CASCADE)
    price=models.IntegerField()
    def __str__ (self):
        return self.name
# Create your models here.
