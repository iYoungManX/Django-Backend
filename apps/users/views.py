from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.users.forms import LoginForm
# Create your views here.
class LoginoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class LoginView(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request,'login.html')

    def post(self,request,*args, **kwargs):
        login_form=LoginForm(request.POST)
        # user_name=request.POST.get('username','')
        # password=request.POST.get('password','')

        ## form_verification

        if login_form.is_valid():
            user_name=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user=authenticate(username=user_name,password=password)

            if user is not None:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'login.html',
                              {'msg':'Username or password is incorrect',
                               'login_form':login_form})

        else:
            return render(request, 'login.html',
                          {'login_form': login_form})


