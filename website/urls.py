from django.conf.urls import url 
from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index')
]