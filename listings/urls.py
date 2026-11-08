from django.urls import path
from . import views
urlpatterns = [
    path("novo/", views.listing_create, name="listing_create"),
    path("<int:pk>/", views.listing_detail, name="listing_detail"),
    path("<int:pk>/editar/", views.listing_edit, name="listing_edit"),
]
