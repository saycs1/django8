'''
Created on 2018. 9. 1.

@author: kgitbank404
'''
from django.urls import path
from .views import *

urlpatterns=[
    path('',index.as_view(),name='index'),
    path('<int:post_id>/', detail, name='detail'),
    
    
    ]