from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home-page'),
    path('about/', views.About.as_view(), name='about-page'),
    path('stories/', views.Stories.as_view(), name='stories-page'),
    path('recipes/', views.Recipes.as_view(), name='recipes-page'),
    path('contact/', views.Contact.as_view(), name='contact-page')
]