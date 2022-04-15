from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View


# Create your views here.

class Welcome(TemplateView):
    template_name = "root/welcome.html"

    def get_context_data(self, **kwargs):
        welcome = super().get_context_data(**kwargs)
        welcome['page_title'] = 'SITE HOME'
        welcome['title'] = 'Root'
        return welcome
