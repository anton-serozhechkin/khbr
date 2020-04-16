from django.shortcuts import render
from .models import *

def main(request):
    data_video = VideoDownloading.objects.filter(is_active=True)
    context = {'data_video': data_video}
    return render(request, 'videooverview/index.html', context)
