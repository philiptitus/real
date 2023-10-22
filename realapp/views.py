from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView,View)
from . import models
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
class Indexview(TemplateView):
 template_name = 'index.html'



class TypeListView(ListView):
 
 model = models.Type




class TypeDetailView(DetailView):
 
 model = models.Type
 context_object_name = 'type_details'
 template_name = 'realapp/type_detail.html'




class TypeCreateView(CreateView):
 model = models.Type
 fields = ("house_type", "dealer_name", "dealer_number")



class TypeUpdateView(UpdateView):
 model = models.Type
 fields = ("dealer_name", "dealer_number")



class TypeDeleteView(DeleteView):
 model = models.Type
 success_url = reverse_lazy("realapp:list")





class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')



