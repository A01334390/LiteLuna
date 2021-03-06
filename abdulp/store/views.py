# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import (
    Notebook,
    NotebookOrder,
    Client,
    Order,
    Page
)

# Create your views here.
class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'index.html',context=None)

# //////// Listing of models ////////
class NotebookList(ListView):
    model = Notebook

class ClientList(ListView):
    model = Client

class PageList(ListView):
    model = Page

class OrderList(ListView):
   context_object_name = 'order'
   queryset = Order.objects.all().prefetch_related('client')

class NotebookOrderList(ListView):
    context_object_name = 'notebookorder'
    queryset = NotebookOrder.objects.all().prefetch_related('order','notebook','page')

# //////// Creation of models ///////////
class NotebookOrderCreation(CreateView):
    model = NotebookOrder
    success_url = reverse_lazy('notebookorder_list')
    fields = ['order','quantity','notebook','status','page']

class OrderCreation(CreateView):
    model = Order
    success_url = reverse_lazy('order_list')
    fields = ['date','priority','client']

class NotebookCreation(CreateView):
    model = Notebook
    success_url = reverse_lazy('notebook_list')
    fields = ['nType','benefit']

class ClientCreation(CreateView):
    model = Client
    success_url = reverse_lazy('client_list')
    fields = ['firstName','secondName','address','isPhysical','email']

class PageCreation(CreateView):
    model = Page
    success_url = reverse_lazy('page_list')
    fields = ['description','cost']

# ////////// Update Viws ///////////
class NotebookOrderUpdate(UpdateView):
    model = NotebookOrder
    success_url = reverse_lazy('notebookorder_list')
    fields = ['order','quantity','notebook','status','page']

class OrderUpdate(UpdateView):
    model = Order
    success_url = reverse_lazy('order_list')
    fields = ['date','priority','client']

class NotebookUpdate(UpdateView):
    model = Notebook
    success_url = reverse_lazy('notebook_list')
    fields = ['nType','benefit']

class ClientUpdate(UpdateView):
    model = Client
    success_url = reverse_lazy('client_list')
    fields = ['firstName','secondName','address','isPhysical','email']

class PageUpdate(UpdateView):
    model = Page
    success_url = reverse_lazy('page_list')
    fields = ['description','cost']

# //////// Delete View //////////
class NotebookOrderDelete(DeleteView):
    model = NotebookOrder
    success_url = reverse_lazy('notebookorder_list')

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

class NotebookDelete(DeleteView):
    model = Notebook
    success_url = reverse_lazy('notebook_list')

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('page_list')

# //////// Detailed View /////////
class NotebookOrderDetail(DetailView):
    context_object_name = 'notebookorder'
    queryset = NotebookOrder.objects.all().prefetch_related('order','notebook','page')

class OrderDetail(DetailView):
    context_object_name = 'order'
    queryset = Order.objects.all().prefetch_related('client')

class ClientDetail(DetailView):
    model = Client

class NotebookDetail(DetailView):
    model = Notebook

class PageDetail(DetailView):
    model = Page