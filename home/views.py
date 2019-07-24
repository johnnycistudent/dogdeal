from django.shortcuts import render

# Create your views here.
def index(request):
    """ Displays Index Page"""
    return render(request, "index.html")