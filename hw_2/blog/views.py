from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = list(Article.objects.values())
    return JsonResponse(articles, safe=False)

def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        return JsonResponse({
            'title': article.title,
            'text': article.text,
            'author': article.author,
        })
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)

