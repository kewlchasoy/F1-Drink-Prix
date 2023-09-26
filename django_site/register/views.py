from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(repsonse):
    if repsonse.method == "POST":
        form = RegisterForm(repsonse.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(repsonse, 'register/register.html', {"form":form})
