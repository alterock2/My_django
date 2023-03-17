from django.shortcuts import render
from users.models import User
from users.forms import UserLoginForm
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
    else:
        form = UserLoginForm()
        context = {'form':  form}
    return render(request, 'users/login.html', context)

def registration(request):
    return render(request, 'users/registration.html')
