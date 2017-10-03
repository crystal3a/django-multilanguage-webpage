from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json

from django.utils.decorators import method_decorator

from .models import Order
from .forms import LoginForm

from django.views.generic import View, FormView


class LoginView(View):
    login_template = "login.html"
    dashboard_template = "/dashboard/"

    def get(self, request):
        login_form = LoginForm()
        return render(request, self.login_template, {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(self.dashboard_template)

            else:
                invalid_login = "Username or password incorrect!"
                return render(request, self.login_template, {'login_form': login_form, 'invalid_login': invalid_login})


class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class AutoCompleteView(FormView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        search_term = data.get("term")
        if search_term:
            users = Order.objects.filter(model__icontains=search_term)
        else:
            users = Order.objects.all()

        results = []
        for user in users:
            user_json = {}
            user_json['id'] = user.id
            user_json['label'] = user.model
            user_json['value'] = user.model
            results.append(user_json)
            data = json.dumps(results)

        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
