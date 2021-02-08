from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy


class SubmitLoginView(LoginView):
    template_name = 'form.html'


class SubmitPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('welcome')

