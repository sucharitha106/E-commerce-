
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

#used to create a new object in the database (in this case, a new user).
class SignUpView(generic.CreateView): 
    form_class    = UserCreationForm #handle new user registration including password confirmation and basic validation.
    success_url   = reverse_lazy('login') #After successful form submission (i.e., new user is created), redirect to the URL with name 'login'.
    template_name = 'signup.html' 