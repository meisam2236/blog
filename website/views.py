from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
import jdatetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

def dateConvertor(date):
    persianDate = str(jdatetime.date.fromgregorian(day=date.day,month=date.month,year=date.year))
    return persianDate.replace('-', '/')

class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        article_data = []
        recentArticles = Article.objects.all().order_by('-createdDate')[1:7]
        for article in recentArticles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url if article.cover.url else None,
                'content': article.content,
                'createdDate': dateConvertor(article.createdDate.date()),
                'category': article.category.title
            })
        lastArticleRaw = Article.objects.latest('createdDate')
        lastArticle = {
            'title': lastArticleRaw.title,
            'cover': lastArticleRaw.cover.url if lastArticleRaw.cover.url else None,
            'content': lastArticleRaw.content,
            'createdDate': dateConvertor(lastArticleRaw.createdDate.date()),
            'category': lastArticleRaw.category.title
            }
        category_data = []
        categories = Category.objects.all()
        context = {
            'article_data': article_data,
            'last_article': lastArticle,
            'categories': categories
        }
        return render(request, 'index.html', context)

class AllArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            allArticles = Article.objects.all().order_by('-createdDate')[:10]
            data = []
            for article in allArticles:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover.url else None,
                    'content': article.content,
                    'createdDate': dateConvertor(article.createdDate.date()),
                    'category': article.category.title,
                    'author': article.author.user.first_name + ' ' + article.author.user.last_name
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            articleTitle = request.GET['article_title']
            article = Article.objects.filter(title__contains=articleTitle)
            serializedData = serializers.SingleArticleSerializer(article, many=True)
            data = serializedData.data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)