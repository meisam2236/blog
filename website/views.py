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

class SearchArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            from django.db.models import Q
            query = request.GET['query']
            articles = Article.objects.filter(Q(content__icontains=query))
            data = []
            for article in articles:
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

class SubmitArticleAPIView(APIView):
    def post(self, request, format=None):
        try:
            serializedData = serializers.SubmitArticleSerializer(data=request.data)
            if serializedData.is_valid():
                title = serializedData.data.get('title')
                cover = request.FILES['cover']
                content = serializedData.data.get('content')
                categoryID = serializedData.data.get('categoryID')
                authorID = serializedData.data.get('authorID')
            else:
                return Response({'status':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(id=authorID)
            author = CustomUser.objects.get(user=user)
            category = Category.objects.get(id=categoryID)
            article = Article()
            article.title = title
            article.cover = cover 
            article.content = content
            article.author = author
            article.category = category
            article.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CoverUpdateArticleAPIView(APIView):
    def post(self, request):
        try:
            serializedData = serializers.CoverUpdateArticleSerializer(data=request.data)
            if serializedData.is_valid():
                articleID = serializedData.data.get('articleID')
                cover = request.FILES['cover']
            else:
                return Response({'status':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            Article.objects.filter(id=articleID).update(cover=cover)
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteArticleAPIView(APIView):
    def post(self, request):
        try:
            serializedData = serializers.DeleteArticleSerializer(data=request.data)
            if serializedData.is_valid():
                articleID = serializedData.data.get('articleID')
            else:
                return Response({'status':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            Article.objects.filter(id=articleID).delete()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)