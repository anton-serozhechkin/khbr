from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from analytics.models import Article
from event.models import Event

def main(request):
    list_rait = Raiting.objects.filter(is_active=True).order_by('-created')    
    context = {'list_rait': list_rait}
    return render(request, 'raitings/index.html', context)

    
def raiting_detail(request, slug):
    data_rait = get_object_or_404(Raiting, slug=slug)
    raiting_images = RaitingImage.objects.filter(raiting__slug=slug)
    data_rait.views += 1
    data_rait.save()
    last_events = Event.objects.filter(is_active=True)[0:1]
    last_analytics = Article.objects.filter(is_active=True)[0:1]
    try:
        next_raiting = data_rait.get_next_by_created()
    except Exception:
        next_raiting=None

    try:
        previous_raiting = data_rait.get_previous_by_created()
    except Exception:
        previous_raiting=None
    return render(request, 'raitings/raiting_detail.html', locals())