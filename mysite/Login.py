from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST["ictasadmin"]
    password = request.POST["ZaK918273*?"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        print ("NOT OK")
        # Return an 'invalid login' error message.
p