from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index ,name="index"),
    path("restaurant/<int:restaurant_id>", views.restaurant_show, name="restaurant")
]