from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method=='POST':
        user=request.POST['text']
        create_pass=request.POST['password1']
        confirm_pass=request.POST['password2']
        email_id=request.POST['email']

        if create_pass==confirm_pass:
            if User.objects.filter(username=user).exists() and User.objects.filter(email=email_id).exists():
                messages.info(request,'Username or Gmail already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user,password=create_pass,email=email_id)
                user.save();
                print('New User Created')
                return redirect('home')
                
        else:
            messages.info(request,'Password Mismatch,Please try again')
            return redirect('register')

        return redirect('/')

    else:

        return render(request,'register.html')

