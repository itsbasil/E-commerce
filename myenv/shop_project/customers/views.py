from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer

# Create your views here.
#logout
def signout(request):
    logout(request)
    return redirect('home')


def show_account(request):
    context={}
    if request.POST and 'register' in request.POST : 
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            #USER account

            user=User.objects.create_user(
            username=username,
            password=password, 
            email=email
            )

            #CUST0MER account
            customer=Customer.objects.create(
            user=user,
            phone=phone,
            address=address
            )
            success_mess='user registered succesfully'
            messages.success(request,success_mess)
        except Exception as e:
            error_message='Same username entered'
            messages.error(request,error_message)
    if request.POST and "login" in request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            logerror='invalid credentials'
            messages.error(request,logerror)



    return render (request,'account.html',context)