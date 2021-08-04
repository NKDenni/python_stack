
from . import views
from django.urls import path

urlpatterns = [
    path('', views.my_post, name='my_post'),
    path('new_note', views.new_note, name='note'),
    path('<int:id>/delete', views.delete),
]