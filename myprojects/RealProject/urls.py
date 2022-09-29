from django.urls import path
from . import views

urlpatterns = [
    path('',views.realProject,),
    path('login',views.loginpage,name='login'),
    path('main',views.mainpage)
]
