from django.shortcuts import render, redirect
from .models import Image

from django.contrib import messages
import datetime as dt

# Create your views here.
def index(request):
    global x
    if request.method == 'POST':
        img = request.FILES.get('image')
        # rename img file
        date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(" ", "_").replace(":", "_")
        img.name = str(date) + '.jpg'
        # print(date, "^^^^^^^^^")
        # print(img.name, "%%%%%%")
        if img is None:
            messages.info(request, 'Please select an image')
            return redirect('index')
        else:
            image = Image(image=img)
            image.save()
            return redirect('result')
    return render(request, 'index.html')

def result(request):
    image = Image.objects.last()
    # print(image.image.url, "$$$$$")
    return render(request, 'result.html', {'image': image})
