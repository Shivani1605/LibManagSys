from django.db import models

# Create your models here.


class Books(models.Model):
    book_name = models.CharField(max_length=100, null=False, blank=False)
    book_quantity = models.IntegerField()
    book_gener = models.TextField()
    status = models.CharField(max_length=20, null=False, blank=False)
    
