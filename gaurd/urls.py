"""gaurd URL Configuration """
from django.urls import path
from gaurd import views

urlpatterns = [
    path('',views.gaurds,name='gaurds'),
    path('ghome',views.ghome,name='ghome'),
    path('glogin',views.glogin,name='glogin'),
    path('glogout',views.glogout,name='glogout'),
    path('insert',views.insert,name='insert'),
    path('enter',views.enter,name='enter'),
    path('exit',views.exit,name='exit'),
    path('update_exit',views.update_exit,name='update_exit'),
    path('chk_entry',views.chk_entry,name='chk_entry'),
    
]
