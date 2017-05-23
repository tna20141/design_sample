from designs import services as design_services

def categories(request):
    return {
        'CATEGORIES': design_services.get_categories(),
    }
