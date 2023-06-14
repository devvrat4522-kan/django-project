"""director URL Configuration """
from django.urls import path
from director import views

urlpatterns = [
    path('',views.director,name='director'),
    path('login',views.login,name='login'),
    path('dhome',views.dhome,name='dhome'),
    path('logout',views.logout,name='logout'),
    path('create',views.create,name='create'),
    path('create_account',views.create_account,name='create_account'),
    path('checkentry',views.checkentry,name='checkentry'),
    
    
]
