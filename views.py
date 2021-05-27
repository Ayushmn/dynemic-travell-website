from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif user.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(firstname=firstname,secondname=secondname,username=username,email=email,password1=password)
                user.save();
                print("user created")

        else:
            messages.info(request,"password error")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
