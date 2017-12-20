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

    def post(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        if lifts[0].last_training == "A":
            return HttpResponseRedirect('/dayb')
        else:
            return HttpResponseRedirect('/daya')


class DayAView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        return render(request, "daya.html", {"lifts": lifts})

    def post(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        for lift in lifts:
            if "deadlift" in request.POST:
                lift.deadlift = lift.deadlift + 2.5
            if "oh_press" in request.POST:
                lift.oh_press = lift.oh_press + 2.5
            if "barbell_row" in request.POST:
                lift.barbell_row = lift.barbell_row + 2.5
            lift.last_training = "A"
            lift.save()
        return HttpResponseRedirect('/lifts')


class DayBView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        return render(request, "dayb.html", {"lifts": lifts})

    def post(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        for lift in lifts:
            if "bench_press" in request.POST:
                lift.bench_press = lift.bench_press + 2.5
            if "squat" in request.POST:
                lift.squat = lift.squat + 2.5
            #lift.pull_ups = max
            lift.last_training = "B"
            lift.save()
        return HttpResponseRedirect('/lifts')
