from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.urls import reverse_lazy

from .models import Item


def index(request):
    all_item_list = Item.objects.order_by('name')
    context = {
        'all_item_list': all_item_list,
    }
    return render(request,'price/index.html',context)


class DetailView(generic.DetailView):
    model = Item
    template_name = 'price/detail.html'


class PersonCreateView(generic.CreateView):
    model = Item
    template_name = 'price/add.html'
    fields = '__all__'
    
    initial = {'pub_date': timezone.now()}
    success_url = reverse_lazy ('price:index')

class ItemUpdate(generic.UpdateView):
    model = Item
    fields = '__all__'
    template_name = 'price/update.html'
    success_url = reverse_lazy ('price:index')

class ItemDelete(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('price:index')


def search_item(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':
        # If the form is submitted
        search_query = request.GET.get('search_box', None)
        all_item_list = Item.objects.filter(name__contains=search_query)
        context = {
            'all_item_list': all_item_list,
        }
        return render (request, 'price/index.html', context)


