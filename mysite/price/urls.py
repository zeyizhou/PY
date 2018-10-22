from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'price'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.add, name = 'Add'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]