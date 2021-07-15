
from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_reg),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
]
