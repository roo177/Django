from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def my_view(request):
    if request.method == 'POST':
        username = request.POST.get('ictasadmin')
        password = request.POST.get('ZaK918273*?')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("Logged in")
            # return render(request, 'success.html')
        else:
            return HttpResponse("Cant log in")
            # Return an 'invalid login' error message.
            # return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return HttpResponse("Login page")
        # return render(request, 'login.html')