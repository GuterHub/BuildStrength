from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Lifts, HistoryA, HistoryB
from datetime import date


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
        history = HistoryA.objects.filter(user=request.user).first()
        for lift in lifts:
            if "deadlift" in request.POST:
                lift.deadlift = lift.deadlift + 2.5
            if "oh_press" in request.POST:
                lift.oh_press = lift.oh_press + 2.5
            if "barbell_row" in request.POST:
                lift.barbell_row = lift.barbell_row + 2.5
            lift.last_training = "A"
            lift.training_count += 1
            lift.save()
            new_deadlift = lift.deadlift
            new_oh_press = lift.oh_press
            new_barbell_row = lift.barbell_row
            new_lifts = HistoryA.objects.create(date=date.today(), deadlift=new_deadlift,
                                                oh_press=new_oh_press, barbell_row=new_barbell_row,
                                                user=request.user)
        return HttpResponseRedirect('/lifts')


class DayBView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        return render(request, "dayb.html", {"lifts": lifts})

    def post(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        history = HistoryB.objects.filter(user=request.user).first()
        for lift in lifts:
            if "bench_press" in request.POST:
                lift.bench_press = lift.bench_press + 2.5
            if "squat" in request.POST:
                lift.squat = lift.squat + 2.5
            if "pull_ups" in request.POST:
                new_value_pull_ups = int(request.POST.get("pull_ups"))
                if new_value_pull_ups > lift.pull_ups:
                    lift.pull_ups = new_value_pull_ups
            lift.last_training = "B"
            lift.training_count += 1
            lift.save()
            new_bench_press = lift.bench_press
            new_squat = lift.squat
            new_pull_ups = lift.pull_ups
            new_lifts = HistoryB.objects.create(date=date.today(), bench_press=new_bench_press,
                                                squat=new_squat, pull_ups=new_pull_ups,
                                                user=request.user)
        return HttpResponseRedirect('/lifts')


class MaxesView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lifts = Lifts.objects.filter(user=request.user)
        ratio = 1.15
        for lift in lifts:
            max_deadlift = float("{0:.1f}".format(lift.deadlift * ratio))
            max_oh_press = float("{0:.1f}".format(lift.oh_press * ratio))
            max_barbell_row = float("{0:.1f}".format(lift.barbell_row * ratio))
            max_bench_press = float("{0:.1f}".format(lift.bench_press * ratio))
            max_squat = float("{0:.1f}".format(lift.squat * ratio))
        return render(request, "maxes.html", {"max_deadlift": max_deadlift,
                                              "max_oh_press": max_oh_press,
                                              "max_barbell_row": max_barbell_row,
                                              "max_bench_press": max_bench_press,
                                              "max_squat": max_squat})


class ProgressView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        historya = HistoryA.objects.filter(user=request.user)
        historyb = HistoryB.objects.filter(user=request.user)
        return render(request, "progress.html", {"historya": historya, "historyb": historyb})


class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            starting_lifts = Lifts.objects.create(deadlift=20, oh_press=20,
                                              barbell_row=20, bench_press=20,
                                              squat=20, pull_ups=5, user=user,
                                              last_training="B", training_count=0)
            login(request, user)
            return redirect('/lifts')
        return render(request, 'signup.html', {'form': form})
