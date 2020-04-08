from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from raitings.models import Raiting
from event.models import Event
from .forms import SubscribeForm

def main(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscribe = form.save(commit=False) 
            email = form.cleaned_data['email']
            form.save()
            return redirect('analytics')
        else:
            return redirect('analytics')
    else:
        form = SubscribeForm()
        data_art = Article.objects.filter(is_active=True).order_by('-created')[0:5]
        data_rait = Raiting.objects.filter(is_active=True).order_by('-created')[0:3]

    return render(request, 'analytics/index.html', locals())

def article_index(request):
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    if data_art:
        context = {'data_art': data_art}
    else:
        context = {'blank': 'К сожалению, ничего не найдено'}
    return render(request, 'analytics/article_index.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'analytics/article_detail.html', locals())

def not_found_view(request, exception):
    return render(request, 'errors/404.html')

def error_view(request):
    return render(request, 'errors/500.html')

def permission_denied_view(request, exception):
    return render(request, 'errors/403.html')

def bad_request_view(request, exception):
    return render(request, 'errors/400.html')

def signup(request):
    return render(request, 'user/signup.html')

def signin(request):
    return render(request, 'user/signin.html')
