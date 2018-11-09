from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm


# Create your views here.
class LoginView(View):
    template_name = 'authorization/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)