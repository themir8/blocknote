from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from .models import Article
from .forms import ArticleEditForm


def Create(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            article_form = ArticleEditForm(request.POST)
            # check whether it's valid:
            if article_form.is_valid():
                Article.objects.update_or_create(
                    title=request.POST.get("title"),
                    body=request.POST.get("body"),
                    author=request.user,
                )
                return redirect(Article.get_absolute_url())
            else:
                error = 'Form is invalid'
        article_form = ArticleEditForm()
        data = {
            'article_form': article_form,
            'error': error
            }
        
        return render(request, 'main/index.html', data)
    else:
        return render(request, 'main/login.html')


def ArticleViewEdit(request, slug):

    data = {
        'el': Article.objects.get(url=slug)
    }

    return render(request, 'main/index.html', data)