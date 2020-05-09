from django.db import models

# Create your models here.
def product_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / <title>/<filename> 
    return '{0}/{1}'.format(instance.title.lower(), filename) 

class Product(models.Model):
    title = models.CharField(max_length=64)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    github_link = models.CharField(max_length=64)
    product_file = models.FileField(upload_to=product_directory_path, default=None, null=True, blank=True)
    icon = models.ImageField(upload_to=product_directory_path, default=None, null=True, blank=True)
    image = models.ImageField(upload_to=product_directory_path, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
