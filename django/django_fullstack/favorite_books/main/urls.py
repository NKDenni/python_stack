
from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_reg),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('new_book', views.new_book),
    path('logout', views.logout),
    path('books/<int:id>', views.details),
    path('books/add/<int:id>', views.add),
    path('books/remove/<int:id>', views.remove),
    path('update/<int:id>', views.update),
    path('books/<int:id>/delete', views.delete),
]
