from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreateNewUser


class CreateNewUserView(CreateView):
    form_class = CreateNewUser
    success_url = reverse_lazy('login')
    template_name = 'accounts/new-user.html'