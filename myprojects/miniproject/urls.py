from django.urls import path
from miniproject import views
from miniproject import index

urlpatterns = [
    path('',views.project),
    path('',index.page1,name='page1'),
    path('page2',index.page2,name='page2'),
    path('page3',index.page3,name='page3'),
    path('familyinfo',views.insfamilyinfo),
    path('fetchfamily',views.fetchfamily),
    path('empinfo',views.empinfo)
]
