from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
        path('signup', views.signup),
         path('home', views.home),
]
