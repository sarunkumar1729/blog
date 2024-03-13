from django import forms 
from account.models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']

class CpassForm(forms.Form):
    old_pass=forms.CharField(max_length=100,label="old password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter old password"}))
    new_pass=forms.CharField(max_length=100,label="new password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter new password"}))
    confirm_pass=forms.CharField(max_length=100,label="confirm password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Re-enter new password"}))


class BlogForm(forms.ModelForm):
        class Meta:
            model=Blogs
            fields=["title","description","image"]
            widgets={
                "title":forms.TextInput(attrs={"class":"form_control"}),
                "description":forms.Textarea(attrs={"class":"form_control"}),
                "image":forms.FileInput(),


            }

class CommentForm(forms.ModelForm):
     class Meta:
          model=comments
          fields=["comment"]
          widgets={
               "comment":forms.Textarea(attrs={"class":"form-control"})
          }