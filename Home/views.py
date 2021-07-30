from . models import Contact
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'Home/index.html')

def about(request):
    return render(request,'Home/about.html')



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = Contact(name=name,email=email,message=message)
        ins.save()
        messages.success(request,"Thank You! We Will Connet With You Soon...")
    return render(request,'Home/contact.html')


def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        user = User.objects.create_user(username,email,pass1)
        user.save()
        messages.success(request,"SIGN SUCCESSFUL...")
        return render(request,'Home/index.html') 
    else:
        return render(request,'Home/index.html')


def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,'LOGIN SUCCESSFUL')           
            return render(request,'Home/index.html') 
    else:
        messages.error(request,"Invalid Crediantions")
        return render(request,'Home/index.html')
    
def handlelogout(request):
    logout(request)
    messages.success(request,'LOGGED OUT SUCCESSFULLY')
    return render(request,'Home/index.html')
