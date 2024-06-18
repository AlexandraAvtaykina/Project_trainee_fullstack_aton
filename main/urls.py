from django.contrib.auth.views import LogoutView
from django.urls import path

from main.apps import MainConfig
from main.views import UserLoginView, RegisterView, ClientListView, ClientCreateView, ClientUpdateView, HomePageView

app_name = MainConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list/', ClientListView.as_view(), name='list'),
    path('login/', UserLoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='update'),
]
