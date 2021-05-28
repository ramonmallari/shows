from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:shows_id>', views.show),
    path('<int:shows_id>/edit', views.edit),
    path('<int:shows_id>/update', views.update),
    path('<int:shows_id>/destroy', views.destroy),
]