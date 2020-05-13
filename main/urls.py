from django.urls import path
from . import views


# Urls built for single page application usage
# It's like very simple API
# Example: GET index, will return only body part of page, 
# then in Javascript I change body part of the page, to new one, that came as response to AJAX request.


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.main),
    path("news", views.news, name='news'),
    path("products", views.products, name='products'),
    path("about", views.about, name="about"),
    path("<int:product_id>", views.product, name="product")
]