from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("haii this is welcome page")

def hello(request):
    return render(request,"chats_sample.html",{'A':"DJANGO",
    'B':[1,2,3,4,5,6],'C':{'name':'python','trainer':'akshay'}})

def lokesh(request,input):
    return render(request,"lokesh.html",{"data":input})

def index(request):
    l1= (['girish',99665588,35,'BANGALORE CANT'],['sai',9966556,25,'chennai'],['gopal',9966446,25,'chennai'])
    return render(request,'index.html',{'data':l1,'d1':"hello world haii"})

def sublokesh(request,input):
    return render(request,"sublokesh.html",{"data":input})

