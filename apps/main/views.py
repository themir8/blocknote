import time
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from .models import Article
from .forms import ArticleEditForm, UserCreationForm
from .services import generate_url


class ArticleList(LoginRequiredMixin, ListView):
	model = Article
	context_object_name = 'articles'


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'main/article.html'


class ArticleCreate(LoginRequiredMixin, CreateView):
	template_name = 'main/create.html'
	form_class = ArticleEditForm

	def form_valid(self, form):
		Article.objects.update_or_create(
			title=self.request.POST.get("title"),
			body=self.request.POST.get("body"),
			author=self.request.user,
			url=slugify(self.request.POST.get("title") + "-" + str(time.strftime("%m-%d")))
			)
		return HttpResponseRedirect(slugify(self.request.POST.get("title") + "-" + str(time.strftime("%m-%d"))))


class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterPage(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

def ArticleViewEdit(request, slug):
    instance = Article.objects.get(url=slug)
    article_form = ArticleEditForm(request.POST or None, instance=instance)
    if article_form.is_valid():
        instance.title=request.POST.get("title")
        instance.body=request.POST.get("body")
        instance.save()
        return redirect('article', slug=slug)
    else:
        error = 'Form is invalid'
    context = {
        'article_form': article_form,
        'error': error,
        'color': 'success',
        'form_status': True,
        'article': instance
    }
    return render(request, 'main/viewedit.html', context)