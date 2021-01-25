from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse('Hello world')

def test(request):
    return render(request, "test.html")

def go(request):
    return render(request, "go.html")

def second(request):
    return HttpResponse("Second test page.")

def third(request):
    return HttpResponse("This is third test page)")
