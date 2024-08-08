from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.URLField(null=True)
    slug = models.SlugField(unique=True,max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
    
class About(models.Model):
    content = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name