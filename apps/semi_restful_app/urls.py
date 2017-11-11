from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^new_dog$', new_dog),
    url(r'^select/(?P<dog_id>\d+)$', select)
]

