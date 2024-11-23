from django.db import models
from django.utils.timezone import now

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200) 
    slug = models.SlugField(unique=True)  
    content = models.TextField() 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def _str_(self):
        return self.title