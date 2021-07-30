from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    post = Posts.objects.all()
    return render(request,'Blog/index.html',{"post":post})

def postdetail(request,id):
    details = Posts.objects.get(id=id)
    return render(request,'Blog/detail.html',{"detail":details})