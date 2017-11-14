from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'main^', include('apps.rescue_mia_app.urls', namespace = 'rescue_mia_app')),
url(r'^', include('apps.login_reg_app.urls', namespace = 'login_reg_app')),
]