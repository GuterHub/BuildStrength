"""BuildStrength URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bs.views import (LoginView, LogoutView, LiftsView,
                      DayAView, DayBView, MaxesView, ProgressView,
                      SignUpView, TestMaxesView, RealMaxesView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^lifts/', LiftsView.as_view(), name="lifts"),
    url(r'^daya/', DayAView.as_view(), name="daya"),
    url(r'^dayb/', DayBView.as_view(), name="dayb"),
    url(r'^maxes/', MaxesView.as_view(), name="maxes"),
    url(r'^progress/', ProgressView.as_view(), name="progress"),
    url(r'^signup/', SignUpView.as_view(), name="signup"),
    url(r'^testmaxes/', TestMaxesView.as_view(), name="testmaxes"),
    url(r'^realmaxes/', RealMaxesView.as_view(), name="realmaxes"),

]
