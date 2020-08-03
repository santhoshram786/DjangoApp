from django.urls import path

from . import views

urlpatterns=[

    path('',views.home,name='home'),
    path('getName',views.getName,name='Players'),
    path('getUser',views.result,name='result'),
    path('logout',views.logout,name='logout')
]