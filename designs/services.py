from django.conf import settings
import os
from .models import Category, Product
import logging

logger = logging.getLogger('django')

def get_categories():
    return Category.objects.all()

def get_products(category_id):
    products = Product.objects.filter(category__id=category_id)
    accepted_exts = ['.jpg', '.jpeg', '.png']
    for product in products:
        product_path = _get_product_path(product.path)
        product.files = [os.path.join(product.path, f) for f in os.listdir(product_path) if os.path.splitext(f)[-1].lower() in accepted_exts]

    return products

def _get_product_path(path):
    return os.path.join(settings.MEDIA_ROOT, path)

