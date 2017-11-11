from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^new_dog$', new_dog),
    url(r'^select/(?P<dog_id>\d+)$', select),
    url(r'^adopted/(?P<dog_id>\d+)$', adopted),
    url(r'^available/(?P<dog_id>\d+)$', available),
    url(r'^select_adopted/(?P<dog_id>\d+)$', select_adopted),
    url(r'^adopted_dogs$', adopted_dogs),

]

