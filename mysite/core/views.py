from django.shortcuts import render

# Create your views here.

def hacker(request):
    return render(request, 'core/hacker.html')