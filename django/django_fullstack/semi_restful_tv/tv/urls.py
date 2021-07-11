from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new, name='shows/new'),
    path('submit', views.submit),
    path('shows/<int:id>', views.show_details, name='show_details'),
    path('shows/<int:id>/edit', views.edit, name='edit'),
    path('shows/<int:id>/update', views.update, name='update'),
    path('shows/<int:id>/destroy', views.destroy, name='destroy'),
]
