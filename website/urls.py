from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('article/all/', views.AllArticleAPIView().as_view(), name='all_articles'),
    path('article/', views.SingleArticleAPIView().as_view(), name='single_article'),
    path('article/search/', views.SearchArticleAPIView().as_view(), name='search_article'),
    path('article/submit/', views.SubmitArticleAPIView().as_view(), name='submit_article'),
    path('article/update-cover/', views.CoverUpdateArticleAPIView().as_view(), name='cover_update_article'),
    path('article/delete/', views.DeleteArticleAPIView().as_view(), name='delete_article'),
]