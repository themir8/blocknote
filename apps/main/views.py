import time
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils.text import slugify
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleEditForm, UserCreationForm


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return Visitor(ip=ip, user=request.user).save()

def ListView(request):
    get_all_posts = Article.objects.filter(author=request.user).all().order_by("-created_date")
    data = {
        'article': get_all_posts
    }
    return render(request, 'main/blog.html', data)

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
                    url=slugify(request.POST.get("title") + "-" + str(time.strftime("%m-%d")))
                )
                return HttpResponseRedirect(slugify(request.POST.get("title") + "-" + str(time.strftime("%m-%d"))))
            else:
                error = 'Form is invalid'
        article_form = ArticleEditForm()
        data = {
            'article_form': article_form,
            'error': error,
            'color': 'dark'
            }
        
        return render(request, 'main/index.html', data)
    else:
        return redirect('login')

# def Registration(request):
#     if(not request.user.is_authenticated):
#         if request.method == 'POST':
#             form = UserRegistrationForm(request.POST)
#             if form.is_valid():
#                 new_user = form.save()
                
#                 return HttpResponseRedirect("/")
#         else:
#             form = UserRegistrationForm()
#         return render(request, "main/registration.html", {
#             'form': form,
#             })
#     else:
#        return HttpResponseRedirect("/")

# def LoginView(request):
#     if(not request.user.is_authenticated):
#         if request.method == "POST":
#             username = request.POST.get('username', '')
#             password = request.POST.get('password', '')
            
#             user = authenticate(
#                 username=username,
#                 password=password
#                 )
#             if user is not None and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect("/")
#             else:
#                 return HttpResponseRedirect("/account/invalid/")
#     else:
#            return HttpResponseRedirect("/") 
    
#     return render(request, 'main/login.html')

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