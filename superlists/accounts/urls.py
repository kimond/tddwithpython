from django.conf.urls import url

from .views import persona_login

urlpatterns = [
    url(r'login$', persona_login, name='persona_login'),
]