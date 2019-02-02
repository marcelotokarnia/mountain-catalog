"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from graphene_django.views import GraphQLView
from mountains.views import index
from core.views import authenticate, get_strava_kml


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^authenticate$', authenticate),
    url(r'^get_strava_kml/(?P<username>[\w.@+-]+)/(?P<seed>[\w.@+-]+)$', get_strava_kml),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'', index, name="index"),
]
