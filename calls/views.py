from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,"sample.html")

def parent(request):
    return render(request,"parent.html")

def child(request):
    return render(request,"child.html")