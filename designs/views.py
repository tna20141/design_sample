from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.conf import settings
import os
from . import services

# Create your views here.
def category(request, category_id):
    try:
        products = services.get_products(category_id)
        for product in products:
            product.files = [_get_media_url(f) for f in product.files]
            product.thumb = product.files[0]
    except Exception:
        return HttpResponse(status=500)
    return render(request, 'gallery.html', { 'products': products }, context_instance=RequestContext(request))

def _get_media_url(path):
    return os.path.join(settings.MEDIA_URL, path)
