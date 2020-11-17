from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LogoutView
from django.urls import reverse

from django.contrib.auth import login as auth_login, get_user_model, logout

from .forms import CustomAuthenticationForm

# Create your views here.

User = get_user_model()

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


class CustomLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('home-page')
    
    def get_user(self, form):
        username = form.cleaned_data.get('username')
        valid_user = User.objects.filter(username=username).first()
        print(valid_user)
        return valid_user
    
    def check_password(self, user, form):
        password = form.cleaned_data.get('password')
        return user.check_password(password)
    
    def form_valid(self, form):
        user = self.get_user(form)
        if user:
            is_valid_password = self.check_password(user, form)
            if is_valid_password:
                auth_login(self.request, user)
                return super().form_valid(form)

    
class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('login-page')