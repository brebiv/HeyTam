from django.db import models
import json

# Create your models here.
def product_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / <title>/<filename> 
    return 'products/{0}/{1}'.format(instance.title.lower(), filename) 

def article_directory_path(instance, filename):
    return 'news/{0}/{1}'.format(instance.title.lower(), filename)

class Product(models.Model):
    title = models.CharField(max_length=64)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    github_link = models.CharField(max_length=64, null=True, blank=True)
    product_file = models.FileField(upload_to=product_directory_path, default=None, null=True, blank=True)
    icon = models.ImageField(upload_to=product_directory_path, default=None, null=True, blank=True)
    image = models.ImageField(upload_to=product_directory_path, default=None, null=True)

    def toDict(self) -> dict:
        return dict({
            "id": self.pk,
            "title": self.title,
            "short_description": self.short_description,
            "description": self.description,
            "github_link": self.github_link,
            "product_file": self.product_file.url,
            "icon": self.icon.url,
            "image": self.image.url
        })

    def __str__(self):
        return f"{self.title}"


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.text} --- {self.author}"


class Article(models.Model):
    title = models.CharField(max_length=64)
    main_text = models.TextField()
    image = models.ImageField(upload_to=article_directory_path, default=None, null=True, blank=True)
    more_link = models.CharField(max_length=64, default=None, null=True, blank=True)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.pub_date}"