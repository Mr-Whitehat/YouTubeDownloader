from django.shortcuts import render
from pytube import *
import os
from django.conf.urls import *
global url
global strms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def download(request):
    global url
    url = request.GET.get('url') #,'')
    if url== "":
        return render(request,'empty.html')
    yt= YouTube(url)
    strms= []
    strms= yt.streams.filter(progressive=True).all
    embed_link= url.replace("watch?v=","embed/")
    Title = yt.title
    params={'title': Title, 'strms': strms, 'embed': embed_link, 'url': url}#, 'size': size}
    return render(request, 'download.html', params)

def yt_download_done(request,resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + "/Downloads"
    if request.method == 'POST':
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request, 'done.html')

    else:
        return render(request, 'error.html')
