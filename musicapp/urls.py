from django.urls import path
from . import views
# from django.conf import

urlpatterns = [
    path("", views.index, name="index"),
]