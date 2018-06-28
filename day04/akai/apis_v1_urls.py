from django.conf.urls import url
from akai import apis_v1 as api

urlpatterns = [
    url(r'^add-language$', api.add_language_api)
]