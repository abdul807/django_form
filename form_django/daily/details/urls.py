from django.urls import path 

from . import views



app_name = 'detail'

urlpatterns = [ 
    path('',views.index,name = 'index'),
    path('signup',views.signup,name='signup'),
    path('addData',views.addData,name='addData'),
    path('home',views.view_data,name='view_data')
]