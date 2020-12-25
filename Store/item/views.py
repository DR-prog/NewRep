from django.shortcuts import render
from django.views.generic import ListView , DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy 
from .models import Item

from django.core.exceptions import PermissionDenied

from django.contrib.auth.mixins import LoginRequiredMixin

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "list_item.html"
    context_object_name = "list_item"
    login_url = 'login'


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item 
    template_name = "detail_item.html"
    context_object_name = "item"
    login_url = 'login'

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ("title", "amount","price")
    template_name = "update_item.html"
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
    
        item = self.get_object()
        if item.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "delete_item.html"
    success_url = reverse_lazy("list_item")
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
       
        item = self.get_object()
        if item.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "new_item.html"
    fields = ('title','price','amount')
    def form_valid(self, form):
       
        form.instance.owner = self.request.user 
        
        return super().form_valid(form)
    
