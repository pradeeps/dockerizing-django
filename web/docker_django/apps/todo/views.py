from django.shortcuts import render, redirect
from .models import Item
from redis import Redis
from django.http import HttpResponse

redis = Redis(host='redis', port=6379)

def home(request):
    return HttpResponse("Hello world from Docker")

def home1(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})
