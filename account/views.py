from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from . forms import LoginForm, RegisterForm

# def user_login(request):
#     return render(request, 'account/login.html' , {})


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("home:main")
            else:
                form.add_error("phone", "invalid user data")
        else:
            form.add_error("phone", "invalid user data")
        return render(request, "account/login.html", {"form": form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render (request, "account/register.html", {"form": form})
        