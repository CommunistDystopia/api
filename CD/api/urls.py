from django.urls import include, path
from rest_framework import routers
from CD.api import views

router = routers.DefaultRouter()

app_name = "api"

urlpatterns = [path("", include(router.urls))]
