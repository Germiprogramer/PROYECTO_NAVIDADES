from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import LoginForm

# Create your views here.

def hacker(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            #!esto hay que cambiar
            if user is not None:
                login(request, user)
                return render(request, 'core/hacker.html')
            else:
                return render(request, 'core/hacker.html')
            
    else:
        form = LoginForm()
    return render(request, 'core/hacker.html')