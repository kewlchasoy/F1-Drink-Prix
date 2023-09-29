from django.shortcuts import render, redirect

def index(request):
  return render(request, 'my_app/index.html')

def f1(request):
  return render(request, 'my_app/f1.html')
