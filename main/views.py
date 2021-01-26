from django.shortcuts import render, HttpResponse
from .models  import (ToDo)

def homepage(request):
   return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html",{"todo_list":todo_list})

def go(request):
    return render(request, "go.html")

def second(request):
    return HttpResponse("Second test page.")

def third(request):
    return HttpResponse("This is third test page)")
