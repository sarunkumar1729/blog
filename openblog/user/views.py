from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView,DeleteView,UpdateView
from .forms import *
from account.models import UserProfile,Blogs
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.http import HttpResponse
# Create your views here.

class userView(CreateView):
    form_class=BlogForm
    model=Blogs
    template_name="userhome.html"
    success_url=reverse_lazy("uh")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Blog Posted")
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Blogs.objects.all().order_by("-date")
        context["cform"]=CommentForm()
        print(context["data"])
        return context
    

def commentadd(request,*args, **kwargs):
    if request.method=='POST':
        bid=kwargs.get("bid")
        blog=Blogs.objects.get(id=bid)
        cmnt=request.POST.get("comment")
        user=request.user
        comments.objects.create(comment=cmnt,user=user,blog=blog)
        messages.success(request,"commented successfully")
        return redirect("uh")


class ProfileView(TemplateView):
    template_name="profile.html"

class EditProfile(View):
        def get(self,request,*args,**kwargs):
            pid=kwargs.get("pid")
            p=UserProfile.objects.get(id=pid)
            f=ProfileForm(instance=p)
            return render(request,"edit.html",{"data":f})
        def post(self,request,*args,**kwargs):  
            pid=kwargs.get("pid") 
            p=UserProfile.objects.get(id=pid)
            form_data=ProfileForm(data=request.POST,files=request.FILES,instance=p)
            if form_data.is_valid():
                form_data.save()
                messages.success(request,"profile updated")
                return redirect("prof")
            else:
                return render(request,"edit.html",{"form":form_data})



class AddProfile(CreateView):
    template_name="addprofile.html"
    form_class=ProfileForm
    model=UserProfile
    success_url=reverse_lazy("prof")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"profile added!!")
        return super().form_valid(form)

    # def post(self,request,*args,**kwargs):
    #     form_data=self.form_class(data=request.POST,files=request.FILES)
    #     if form_data.is_valid():
    #         form_data.instance.user=request.user
    #         form_data.save()
    #         return redirect("prof")
    #     else:
    #         return render(request,"addprofile.html",{"form":form_data})

class cpassView(FormView):
    template_name="cpass.html"
    form_class=CpassForm
    def post(self,request,*args,**kwargs):   
        form=self.form_class(data=request.POST)
        if form.is_valid():
            old=form.cleaned_data.get("old_pass")
            new=form.cleaned_data.get("new_pass")
            cnf=form.cleaned_data.get("confirm_pass")
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new==cnf:
                    # user.password=new
                    # user.save()
                    user.set_password(new)
                    user.save()
                    logout(request)
                    messages.success(request,"password changed!!")
                    return redirect("log")
                else:
                    messages.error(request,"password mismatch")
                    return redirect("cpass")
            else:
                messages.error(request,"old password entered is incorrect ")
                return redirect("cpass")


class myBlogView(TemplateView):
    template_name="myblogs.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Blogs.objects.filter(user=self.request.user).order_by('-date')
        return context

class DeleteBlog(DeleteView):
    model=Blogs
    success_url=reverse_lazy("myb")
    template_name="deleteblog.html"


class EditBlog(UpdateView):
    model=Blogs
    success_url=reverse_lazy("myb")
    template_name="editblog.html"
    form_class=BlogForm







      
