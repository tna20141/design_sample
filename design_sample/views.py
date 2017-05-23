from django.template import loader, RequestContext
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from design_sample.forms import ContactForm
import logging

logger = logging.getLogger('django')

@cache_page(3600)
def index(request):
    return render(request, 'index.html', {}, context_instance=RequestContext(request))

@csrf_exempt
def send_contact(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        response = JsonResponse(form.errors, status=422)
        return response

    logger.info('mail sent')

    return HttpResponse()
