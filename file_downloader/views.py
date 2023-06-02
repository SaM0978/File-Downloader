from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import settings
import requests
import os
import time

def download(url):
    request = requests.get(url, stream=True)
    name = url.split('/')[-1]
    if '?' in url:
        while True:
            name = input('Enter The Name Of The File With Extension')
            if '.' not in name:
                print('Enter The Extension')
            else:
                break
    
    with open(f"{os.path.join(settings.BASE_DIR, 'media')}/{name}", 'wb') as file:
        for i in request.iter_content(chunk_size=1024):
            file.write(i)

    return ['Done', name]


@csrf_exempt
def index(request):
    Val = ['', '']
    if request.method == 'POST':
        url = request.POST.get('url')
        Val = download(url)
    
    return render(request, 'index.html', {'Done': Val[0], "name": Val[1]})