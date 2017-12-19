from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Lifts


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth = authenticate(username=username, password=password)
            if auth:
                login(request, auth)
                return HttpResponseRedirect('/lifts')
            else:
                return HttpResponse("Błędny login lub hasło!")
        return render(request, "form.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')


class LiftsView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        return render(request, "lifts.html", {"lifts": lifts})


class DayAView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        return render(request, "daya.html", {"lifts": lifts})


class DayBView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        return render(request, "dayb.html", {"lifts": lifts})
