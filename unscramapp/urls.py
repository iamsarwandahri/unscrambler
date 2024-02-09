from django.urls import path
from unscramapp import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),

]