from django.contrib import admin
from .models import Product, Quote, Article

# Register your models here.
admin.site.register(Product)
admin.site.register(Quote)
admin.site.register(Article)