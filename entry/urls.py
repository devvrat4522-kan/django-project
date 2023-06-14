"""entry URL Configuration """
from django.contrib import admin
from django.urls import path,include
from entry import views

admin.site.site_header ="Entry & exit system "
admin.site.site_title ="Entry & exit system "
admin.site.index_title ="Entry & exit system "

urlpatterns = [
    path('', views.index,name='index'),
    path('director/', include('director.urls')),
    path('gaurd/', include('gaurd.urls')),
    path('admin/', admin.site.urls),
]
