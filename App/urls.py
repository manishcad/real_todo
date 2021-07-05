from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("update/<str:pk>", views.update, name="update"),
    path("signup", views.sign_up, name="signup"),
    path("login", views.loginpage, name="login"),
    path("logout", views.logout_page, name="logout"),
]
