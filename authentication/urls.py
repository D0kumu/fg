from django.urls import path

from . import views

urlpatterns = [
    path('', views.auth, name="auth"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="logout"),
]
