from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
     
# from calc.forms import EntryForm

# def ins(request):
#     form = EntryForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()

#     return render(request, 'home.html', {'form': form})

  
# Create your views here.
def home(request):
    #return HttpResponse("Hello World")
    return render(request,'home.html',{'name':'Everyone'})
 
def getName(request):

    if request.method=='POST':
        user=request.POST['text']
        passw=request.POST['password']

        user=auth.authenticate(username=user,password=passw)

        if user is not None:
            auth.login(request,user)
            return redirect("result")
        else:
            messages.info(request,'Not a Valid User')
            return redirect("home")


    else:
        return render(request,'home.html')


def result(request):
    return render(request,'result.html')


def logout(request):
    
    return render(request,'home.html')   