from django.urls import path,include
from DBoperations import views

urlpatterns=[
    path('home',views.Homepage,name='home'),
    path('fetchemp',views.FetchEmpdata,name='fetchemp'),
    
    path('orminsert',views.orminsertdata,name='orminsert'),
    path('ormselect',views.ormFetchData,name='ormselect'),
    
    path('insfam',views.FamDetailes,name='insfam'),
    path('fetchfam',views.FetchFamdata,name='fetchfam'),
    path('insprod',views.PDetailes,name='insprod'),
    path('fetchprod',views.fetchproduct),
    path('form',views.formexp),
    
]

