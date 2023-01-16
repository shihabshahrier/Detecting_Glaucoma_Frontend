from django.shortcuts import render, redirect
from .models import Image
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        img = request.FILES.get('image')
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
    print(image.image.url, "$$$$$")
    return render(request, 'result.html', {'image': image})
