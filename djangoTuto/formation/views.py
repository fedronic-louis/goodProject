from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Message index de votre projet 'Formation'.")
    return render(request, "index.html", {})
