from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm, UserRegistrationForm
from django.shortcuts import redirect


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


#  Форма для регистрации юзера
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', context={'user_form': user_form})
