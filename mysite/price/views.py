from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Item



def index(request):
    all_item_list = Item.objects.order_by('name')
    context = {
        'all_item_list': all_item_list,
    }
    return render(request,'price/index.html',context)


def add(request):
    return HttpResponse ("THIS IS THE ADD PAGE")

