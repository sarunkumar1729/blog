from django.urls import path
from .views import *

urlpatterns = [
    path('userhome/',userView.as_view(),name="uh"),
    path('profile/',ProfileView.as_view(),name="prof"),
    path('addprofile/',AddProfile.as_view(),name="addpro"),
    path('cpassword/',cpassView.as_view(),name="cpass"),
    path('edit/<int:pk>',EditProfile.as_view(),name="ed"),
    path('myblog/',myBlogView.as_view(),name="myb"),
    path('deleteblog/<int:pk>',DeleteBlog.as_view(),name="dlt"),
    path('editblog/<int:pk>',EditBlog.as_view(),name="edt"),
    path('addc/<int:bid>',commentadd,name="cmnt")



    ]
