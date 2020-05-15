from django.test import TestCase, Client
from .models import Product

import tempfile

# Temporary image file to fill image field while testing.
temp_img = tempfile.NamedTemporaryFile(suffix=".jpg").name

# Create your tests here.
class MainTestCase(TestCase):

    def setUp(self):
        p1 = Product.objects.create(title="Test product 1",
                                    short_description="Product for testing 1",
                                    description="Big description of test product 1",
                                    image=temp_img)
        p2 = Product.objects.create(title="Test product 2",
                                    short_description="Product for testing 2",
                                    description="Big description of test product 2",
                                    image=temp_img)

    def testIndex(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_valid_product_page(self):
        """Check if id is valid"""
        p = Product.objects.get(title="Test product 1")

        c = Client()
        response = c.get(f"/{p.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_product_page(self):
        """Check if id is invalid"""
        max_id = Product.objects.all().last().id

        c = Client()
        response = c.get(f"/{max_id+1}")
        self.assertEqual(response.status_code, 404)