from django.conf.urls import url,include
from . import views


urlpatterns = [
    url('^$',views.home,name = 'home'),
url(r'^accounts/', include('registration.backends.simple.urls')),
]