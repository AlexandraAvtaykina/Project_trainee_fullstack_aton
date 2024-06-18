from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView

from main.forms import UserLoginForm, UserRegisterForm, ClientForm, ClientStatusForm
from main.models import User, Client


class HomePageView(TemplateView):
    template_name = 'main/base.html'


class UserLoginView(LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('main:list')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'main/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse_lazy('main:list')


class ClientListView(ListView):
    model = Client
    template_name = 'main/list.html'

    def get_queryset(self):
        client = super().get_queryset()
        return client.filter(fullname_of_the_person_responsible=self.request.user)


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'main/client_form.html'
    success_url = reverse_lazy('main:list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.fullname_of_the_person_responsible = self.request.user
            new_client.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientStatusForm
    template_name = 'main/client_form_status.html'
    success_url = reverse_lazy('main:list')


