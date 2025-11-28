from django.db import models
from django.contrib import admin
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200,help_text="Enter the book title")
    author = models.CharField(max_length=100,help_text="Enter the author's name")
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13,help_text="Enter the ISBN number")
  
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn_number')
    