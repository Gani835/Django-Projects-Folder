from django.urls import path
from javascript import views
urlpatterns = [
    path('',views.change_content),
    path('db',views.dialogue_box),
    path('chimg',views.change_image),

# JavaScript . . . . . 
   path('validate',views.jsvalidate),
]
