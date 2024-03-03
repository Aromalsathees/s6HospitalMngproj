from django.shortcuts import render,redirect
from . models import *
from . forms import *

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm






# Create your views here.


def checking(request):
    return render(request,'checking.html')






def home(request):

    if request.method=='POST':
        form=Bookingforms(request.POST)

        if form.is_valid:
            form.save()
            messages.info(request,'Your slot has Booked')
          


    serv=ourservice.objects.all()
    doct=ourdocters.objects.all()
    blood=Bloodavailabilty.objects.all()
    form=Bookingforms()
    blog=articles.objects.all()


    context={


        'serv':serv,
        'blood':blood,
        'doct':doct,
        'form':form,
        'blog':blog,
    }
        
        
    return render(request,'home.html',context)





def profile(request,id):

    if request.method=='POST':
        form=doctersBookingforms(request.POST)

        if form.is_valid:
            form.save()
            messages.info(request,'Your slot has booked')


    

    form=doctersBookingforms()
    doct=ourdocters.objects.get(id=id)
   
    context = {
        'doct':doct,
        'form':form,
    }

    return render(request,'docters_profile.html',context)

   
    
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            # Add an error message for incorrect credentials
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('home')



# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             return redirect('login/')  # Redirect to login page if authentication fails

#     return render(request, 'login.html')





def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email address already exists')
                return redirect('signup')
            else:
                user_reg = User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                return redirect('home')
        else:
                messages.info(request, 'Passwords do not match')
                return redirect('signup')
    else:
        return render(request, 'signup.html')
    


def prescription(request):

    context = {
        'medicine':prescribed.objects.filter(Prescription__patient__name=request.user)
    }
    return render(request,'prescription.html',context)    
    


            




