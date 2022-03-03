from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("service/", views.service),
    path("partners/", views.partners),
    path("about/", views.about),
    path("contact/", views.contact)
]