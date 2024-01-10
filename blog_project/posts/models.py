from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(default = None)
    category = models.ManyToManyField(Category) # a post can have mutiple category and also a category can have multiple posts
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title