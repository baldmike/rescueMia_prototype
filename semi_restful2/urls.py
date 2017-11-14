from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^', include('apps.rescue_mia_app.urls', namespace = 'rescue_mia_app'))
]