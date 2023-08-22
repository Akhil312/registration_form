from . import views
from django.urls import path

urlpatterns = [

    path('',views.page1,name='page1')


   # path('add/',views.additions,name="additions")

]