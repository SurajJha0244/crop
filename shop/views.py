from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import product,contact,Crop_Recommend
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as ln,logout
from django.contrib import messages
import joblib,os, numpy as np
model_path = os.path.join(settings.BASE_DIR, 'shop', 'static', 'decision_tree_model.pkl')
model = joblib.load(model_path)
def index(request):
    return render(request,'shop/index.html')

def about(request):
    # return render('request','shop/index.html')
    return render(request,'shop/about.html')

def home(request):
    return render(request,'shop/home.html')

def terms(request):
    return render(request,'shop/terms.html')

def result(request):
    return render(request,'shop/result.html')

def user_contact(request):
    if request.method =="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        # print(name,email,phone,desc)
        ncontact=contact(name=name,email=email,phone=phone,desc=desc)
        ncontact.save()
    return render(request,'shop/contactus.html')

def Crop_recommend(request):
    import os
import numpy as np
import joblib
from django.shortcuts import render
from django.conf import settings

def Crop_recommend(request):
    if request.method == 'POST':
        try:
            # Extract inputs and convert to float
            nitrogen = float(request.POST.get('N', 0))
            phosphorus = float(request.POST.get('P', 0))
            potassium = float(request.POST.get('K', 0))
            temperature = float(request.POST.get('temperature', 0))
            humidity = float(request.POST.get('humidity', 0))
            ph = float(request.POST.get('pH', 0))
            rainfall = float(request.POST.get('rainfall', 0))

            input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

            # Load the model
            model_path = os.path.join(settings.BASE_DIR, 'shop', 'static', 'decision_tree_model.pkl')
            model = joblib.load(model_path)

            # Load the label encoder
            encoder_path = os.path.join(settings.BASE_DIR, 'shop', 'static', 'label_encoder.pkl')
            label_encoder = joblib.load(encoder_path)

            # Predict the label number
            predicted_label_num = model.predict(input_data)[0]

            # Inverse transform to get original crop name string
            prediction = label_encoder.inverse_transform([predicted_label_num])[0]

            return render(request, 'shop/service.html', {'crop': prediction})

        except Exception as e:
            return render(request, 'shop/service.html', {'error': str(e)})

    return render(request, 'shop/service.html')



    # if request.method == "POST":
    #     N = float(request.POST.get('N', 0))
    #     P = float(request.POST.get('P', 0))
    #     K = float(request.POST.get('K', 0))
    #     rainfall = float(request.POST.get('rainfall', 0))
    #     ph = float(request.POST.get('pH', 0)) 
    #     temperature = float(request.POST.get('temperature', 25))  
    #     humidity = float(request.POST.get('humidity', 50))  
        
    #     Crop_Recommend.objects.create(
    #         Nitrogen=N,
    #         Phosphorus=P,
    #         Potassium=K,
    #         Rainfall=rainfall,
    #         pH=ph 
    #     )

    #     return render(request, 'shop/service.html', {'result': 'Data saved successfully'})
    
    # return render(request, 'shop/service.html')


def user_login(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user= authenticate(username=loginusername,password=loginpassword)
        
        if user is not None:
            ln(request,user)
            messages.success(request,"successfully logged in.")
            return redirect('shop:home')
        else:
            messages.error(request,'invalid credecntials.')
            return redirect('login')
    return render(request,'shop/login.html')  

def user_logout(request):
    if request.method=='POST':
        logout(request)
        messages.success(request,"successfully logout")
        return redirect('shop:home')

def user_signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        # print("Creating user:", username)
         
        if not username.isalnum():
            messages.success(request,'username must be alphanumeric')
            return redirect('shop:signup')
        if (password1 != password2):
            messages.success(request,'password doesnt match')
            return redirect('shop:signup')
        
        myuser=User.objects.create_user(username=username, email=email, password=password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        
        messages.success(request,'your account has been logged in')
        return redirect('shop:home')
    else:
        return render(request, 'shop/signup.html')
        # return HttpResponse("404- Not found")          
      
    


