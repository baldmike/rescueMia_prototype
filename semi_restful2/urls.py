from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^', include('apps.semi_restful_app.urls', namespace = 'semi_restful_app'))
]