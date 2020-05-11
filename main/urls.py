from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.main),
    path("products", views.products, name='products'),
    path("about", views.about, name="about"),
    path("<int:product_id>", views.product, name="product")
]