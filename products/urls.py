from django.conf.urls import url, include
from .views import all_dogs_selling, view_dog_ad, wanted_dogs, add_dog_sale_ad, delete_dog_sale_ad, view_wanted_dog_ad, add_dog_wanted_ad, edit_dog_sale_ad, delete_dog_wanted_ad, add_comment, delete_comment

urlpatterns = [
    url(r'^$', all_dogs_selling, name='dogs_for_sale'),    
    url(r'^wanted_dogs$', wanted_dogs, name='wanted_dogs'),
    url(r'^(?P<pk>\d+)/$', view_dog_ad, name='view_dog_ad'), 
    url(r'^add_sale/$', add_dog_sale_ad, name='add_dog_sale_ad'), 
    url(r'^(?P<pk>\d+)/edit_dog_sale_ad/$', edit_dog_sale_ad, name='edit_dog_sale_ad'),
    url(r'^(?P<pk>\d+)/delete_dog_sale_ad/$', delete_dog_sale_ad, name='delete_dog_sale_ad'), 
    url(r'^wanted_dogs/(?P<pk>\d+)/$', view_wanted_dog_ad, name='wanted_dog_ad'), 
    url(r'^add_wanted/$', add_dog_wanted_ad, name='add_dog_wanted_ad'), 
    url(r'^(?P<pk>\d+)/delete_dog_wanted_ad/$', delete_dog_wanted_ad, name='delete_dog_wanted_ad'), 
    url(r'^(?P<pk>\d+)/add_comment/$', add_comment, name='add_comment'), 
    url(r'^(?P<pk>\d+)/delete_comment/$', delete_comment, name='delete_comment'), 
]