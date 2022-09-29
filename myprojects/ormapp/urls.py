from django.urls import path
from ormapp import views
urlpatterns = [
    path('',views.amazonprod),
    path('fetchprod/',views.fetchprod),
    path('prodform/',views.prodform)
]
