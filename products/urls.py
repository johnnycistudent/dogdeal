from django.conf.urls import url, include
from .views import all_dogs_selling, view_dog_ad

urlpatterns = [
    url(r'^$', all_dogs_selling, name='dogs_for_sale'),    
    url(r'^(?P<pk>\d+)/$', view_dog_ad, name='view_dog_ad'), 
]