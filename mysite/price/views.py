import json

from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
from .models import Item
from django.views import generic


def index(request):
    all_item_list = Item.objects.order_by('name')
    context = {
        'all_item_list': all_item_list,
    }
    return render(request,'price/index.html',context)


def add(request):
    return HttpResponse ("THIS IS THE ADD PAGE")


class DetailView(generic.DetailView):
    model = Item
    template_name = 'price/detail.html'
