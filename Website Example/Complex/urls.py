from django.urls import path

from . import views

urlpatterns = [

    path("register/", views.register_view, name="register_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path('home/', views.home_view, name='home_view'),
    path('contact/', views.contact_view, name='contact_view'),
]
