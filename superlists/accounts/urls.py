from django.conf.urls import url
from django.contrib.auth.views import logout

from .views import persona_login

urlpatterns = [
    url(r'^login$', persona_login, name='persona_login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]