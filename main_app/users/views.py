from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def persons(request):
    users = CustomUser.objects.filter(is_superuser=False).order_by('username')
    return render(request, 'planner/all_persons.html', {'users': users})