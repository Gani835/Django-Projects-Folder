from django.urls import path
from . import views

urlpatterns = [
    path('',views.Project),
    path('login',views.loginpage),
    path('main',views.mainpage)
]
