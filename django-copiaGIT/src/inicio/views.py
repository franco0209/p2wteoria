from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args, **kwargs):
    myContext={
        "myText":"Esto nosotros",
        "myNumber": 123,
    }
    return render(request, "home.html", myContext)

def anotherView(request):
    return HttpResponse("<h1> Otra página </h1>")