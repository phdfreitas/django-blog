from django.urls import path
from . import views


urlpatterns = [
    path('newAccount', views.CreateNewUserView.as_view(), name='cadastrarUsuario'),
] 