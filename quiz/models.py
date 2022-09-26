from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"    

class Quiz(models.Model):
    title = models.CharField(max_length=50,verbose_name="Quiz Title")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title