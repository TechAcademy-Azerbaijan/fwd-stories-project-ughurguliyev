from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class Stories(TemplateView):
    template_name = 'strories.html'


class Recipes(TemplateView):
    template_name = 'recipes.html'


class Contact(TemplateView):
    template_name = 'contact.html'