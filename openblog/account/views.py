from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,FormView
from .forms import RegForm,LogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
class HomeView (TemplateView):
        template_name="mainhome.html"


class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('h')

# class Regview(View):
#     def get(self,request,*args,**kwargs):
#         f=RegForm()
#         return render(request,"reg.html",{"form":f})
#     def post(self,request,*args,**kwargs):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"User Registration Successfully!!")
#             return redirect("h")
#         else:
#             messages.error(request,"User Registered faild!!!")
#             return render(request,"reg.html",{"form":form_data})

# class LogView(View):
#     def get(self,request,*args,**kwargs):
#         f=LogForm()
#         us=request.user
#         return render(request,"login.html",{"form":f,"user":us})
#     def post(self,request,*args,**kwargs):   
#         form_data=LogForm(data=request.POST)
#         if form_data.is_valid():
#             un=form_data.cleaned_data.get("uname")
#             ps=form_data.cleaned_data.get("pswd")
#             user=authenticate(request,username=un,password=ps)
#             if user:
#                 login(request,user)
#                 messages.success(request,"User login successfully")
#                 return redirect("uhome")
#             else:
#                 messages.error(request,"login Failed")
#                 return redirect("log")
#         else:
#             return render(request,"login.html",{"form":form_data})

class LogView(FormView):
    form_class=LogForm
    template_name="login.html"
    def post(self,request,*args,**kwargs):   
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("uname")
            ps=form_data.cleaned_data.get("pswd")
            user=authenticate(request,username=un,password=ps)
            if user:
                login(request,user)
                messages.success(request,"User login successfully")
                return redirect("uh")
            else:
                messages.error(request,"login Failed")
                return redirect("log")
        else:
            return render(request,"login.html",{"form":form_data})

class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect("log")
