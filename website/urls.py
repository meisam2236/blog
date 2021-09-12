from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('article/all/', views.AllArticleAPIView().as_view(), name='all_articles'),
    path('article/', views.SingleArticleAPIView().as_view(), name='single_article')
]