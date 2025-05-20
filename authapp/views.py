#authapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm


class HomeView(View):
    def get(self, request):
        return render(request, 'authapp/home.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'authapp/profile.html'

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'authapp/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'authapp/register.html', {'form': form})
