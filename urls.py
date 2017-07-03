from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^search/', include('search.urls')),
    #url(r'^bayesian/', include('bayesian.urls')),
    #url(r'^speciality/', include('speciality.urls')),
    #url(r'^diagnostics/', include('diagnostics.urls')),
    #url(r'^rxnorm/', include('rxnorm.urls')),
    #url(r'^chatbot/', include('chatbot.urls')),
    url(r'^medibot/', include('medibot.urls')),
    url(r'^moleinfo/', include('moleinfo.urls')),
    url(r'^speech2text/', include('speech2text.urls')),
]
