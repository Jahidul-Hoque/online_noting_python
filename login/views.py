from django.shortcuts import render
from login.forms import SignUpForm
from login.forms import ProfilePic
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from django.shortcuts import reverse
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
def signup(request):
    form=SignUpForm()
    registered=False
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True
    dict={'form':form,'registered':registered}
    return render(request,'login/signup.html',context=dict)
def applogin(request):
    form=AuthenticationForm()
    reg=True
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request,'login/applogin.html',context={'form':form,'reg':reg})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:applogin'))

@login_required
def profile(request):
    return render(request,'login/profile.html',context={})
# Create your views here.

@login_required
def add_pro_pic(request):
    form=ProfilePic()
    if request.method=='POST':
        form=ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('login:profile'))
    return render(request,'login/propicadd.html',context={'form':form})