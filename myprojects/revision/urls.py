from django.urls import path
from . import views

urlpatterns = [

   path('',views.userLogin,name='login'),
   path('logout',views.userLogout),
   path('SignUp',views.createUser,name='signup'),
   path('orm',views.Revision),
   path('image',views.imageprocessing),
   path('products',views.productpage,),
  
   # Dynamic Url. . . .
   #path('<value>',views.dynurl,name='product'),
   path('products/<value>',views.dynamicURL,),
   path('proddetailes',views.proddetailes),
   
   # Class Based Views. . . . .
   
   path('class',views.Myview.as_view(),name='class'),
   # CreateView. . . 
   path('createstudent',views.StudentForm.as_view(),name='stdnt'),
   # ListView
   path('studentlist',views.StudentList.as_view()),
   # TemplateView
   #path('template',views.TemplateViewExample.as_view()),
   # DetailView
   path('detail/<pk>',views.StudentDetail.as_view()),
   # UpdateView
   path('<pk>/update/',views.StudentUpdate.as_view()),
   # DeleteView
   path('<pk>/delete',views.StudentDelete.as_view(),name=''),
   

]
