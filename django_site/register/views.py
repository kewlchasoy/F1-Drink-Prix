from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.messages import success

def login(request):
  # Login the user
  ...

  # Flash a message if login is successful
  success(request, "You have successfully logged in!")

  # Redirect the user to the home page
  return redirect("/")
# Create your views here.

def register(repsonse):
    if repsonse.method == "POST":
        form = RegisterForm(repsonse.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(repsonse, 'register/register.html', {"form":form})
