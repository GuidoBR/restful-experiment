from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework import routers
from restfulexperiment.restful import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),

    url(r'^api/v1/users/$', views.user_collection),
    url(r'^api/v1/user/(?P<pk>[0-9]+)$', views.user_element)
]
