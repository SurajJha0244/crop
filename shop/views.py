from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import product,contact,crop_recommend
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as ln,logout
from django.contrib import messages
import joblib,os, numpy as np,json

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def home(request):
    return render(request,'shop/home.html')

def terms(request):
    return render(request,'shop/terms.html')

def result(request):
    return render(request,'shop/result.html')

@login_required
def recommendation_history(request):
    history = crop_recommend.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'shop/history.html', {'history': history})

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


MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'models', 'scaler.pkl')
LABEL_ENCODER_PATH = os.path.join(settings.BASE_DIR, 'models', 'label_encoder.pkl')

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)

@login_required
def Crop_recommend(request):
    crop = None
    history = crop_recommend.objects.filter(user=request.user).order_by('-timestamp')
    if request.method == 'POST':
        try:
            
            N = float(request.POST.get('N'))
            P = float(request.POST.get('P'))
            K = float(request.POST.get('K'))
            temperature = float(request.POST.get('temperature'))
            humidity = float(request.POST.get('humidity'))
            pH = float(request.POST.get('pH'))
            rainfall = float(request.POST.get('rainfall'))

            features = [[N, P, K, temperature, humidity, pH, rainfall]]
            features_scaled = scaler.transform(features)

            pred_encoded = model.predict(features_scaled)[0]
            crop = label_encoder.inverse_transform([pred_encoded])[0]
            
            crop_recommend.objects.create(
            user=request.user,
            nitrogen=N,
            phosphorus=P,
            potassium=K,
            temperature=temperature,
            humidity=humidity,
            ph=pH,
            rainfall=rainfall,
            predicted_crop=crop
        )

        except Exception as e:
            crop = f"Error: {e}"
            
        

    context = {
        'crop': crop,
        'N': request.POST.get('N', 60),
        'P': request.POST.get('P', 30),
        'K': request.POST.get('K', 30),
        'temperature': request.POST.get('temperature', 25),
        'humidity': request.POST.get('humidity', 50),
        'pH': request.POST.get('pH', 6.5),
        'rainfall': request.POST.get('rainfall', 100),
        'history': history
    }
    return render(request, 'shop/service.html', context)



def user_login(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user= authenticate(username=loginusername,password=loginpassword)
        
        if user is not None:
            ln(request,user)
            messages.success(request,"Successfully Logged In. Welcome!!")
            return redirect('/shop/service/')
        else:
            messages.error(request,'Invalid Credentials. Please Enter Valid Credentials.')
            return redirect('/shop/login/')
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
          
      
    


