from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'users/register_form.html', {'form': form})