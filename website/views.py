from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):

   if request.method == 'POST':
    username = request.POST['user_name']
    password = request.POST['password']
    #authenticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
       login(request, user)  #this build in login function will create a session
       messages.success(request, "you have Been  Logged In!")
       return redirect('home')
    else:
       messages.success(request, "There was An Error, please try again!!")
       return redirect('home')
   else:
    return render(request, 'home.html', {})
    
       
   



def logout_user(request):
    pass
