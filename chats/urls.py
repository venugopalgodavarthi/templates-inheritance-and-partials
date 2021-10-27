from django.urls import path
from chats import views
urlpatterns=[
    path("hello/",views.hello,name="hello"),
    path("lokesh/<input>/",views.lokesh,name="lokesh"),
    path('index/',views.index, name="index"),
    path('sublokesh/<input>/',views.sublokesh, name="sublokesh"),
    ]