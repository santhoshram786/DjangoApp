from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    
    dest1=Destination()
    dest2=Destination()
    dest3=Destination()

    dest1.name='Wanaparthy'
    dest1.desc='The District in Telangana with awesome air to breathe'
    dest1.price=1000
    dest1.img='wnp.jpg'
    dest1.offer=True

    dest2.name='Nagar Kurnool'
    dest2.desc='The District in Telangana with awesome dust to Sweep'
    dest2.price=900
    dest2.img='nag.jpg'
    dest2.offer=False

    dest3.name='Gadwal'
    dest3.desc='The District in Telangana with awesome road to walk'
    dest3.price=856
    dest3.img='gadwal.jpg'
    dest3.offer=True

    dest=[dest1,dest2,dest3]

    return render(request,'index.html',{'dests':dest})