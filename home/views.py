from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# password of Anshika user is anshi@000
# Create your views here.
def index(request):
    # print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        # print(f"Received data - Username: {username}, Password: {password}")

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            print("User authenticated successfully.")
            return redirect('/')

        else:
            print("Authentication failed.")
            return render(request,'login.html')
        
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
    