from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
import jdatetime

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
                'cover': article.cover.url,
                'content': article.content,
                'createdDate': dateConvertor(article.createdDate.date()),
                'category': article.category.title
            })
        lastArticleRaw = Article.objects.latest('createdDate')
        lastArticle = {
            'title': lastArticleRaw.title,
            'cover': lastArticleRaw.cover.url,
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