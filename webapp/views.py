from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class helloview(View):
    def get(self,request):
        return HttpResponse('<h1>Welcome</h1>')
class tempview(TemplateView):
    template_name='myapp/results.html'

class contextview(TemplateView):
    template_name = 'myapp/emp.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='durga'
        context['age']=25
        context['marks']=98
        return context
