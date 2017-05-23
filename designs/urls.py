from django.conf.urls import url, include
from . import views

ajaxpatterns = [

]

urlpatterns = [
    url(r'^category/view/([^/]+)/', views.category, name='category_view'),

    url(r'^ajax/', include(ajaxpatterns)),
]
