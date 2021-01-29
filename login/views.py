from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    form = AuthenticationForm
     
    return render(request, 'login1.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/dashview")
    else:
        form = UserCreationForm()
    return render(request, 'signup2.html', {'form': form})

def log_on(request): 
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('dashview')
    else:
        return HttpResponse("invalid")

def log_out(request):    
    logout(request)    
    return redirect('index')

    