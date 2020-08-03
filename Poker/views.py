from django.shortcuts import render

# Create your views here.
def poker(request):
    #return HttpResponse("Hello World")
    return render(request,'index_1.html')