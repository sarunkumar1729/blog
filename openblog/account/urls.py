from django.urls import path
from.views import *

urlpatterns = [
    path('registration',RegView.as_view(),name="reg"),
    path('login/',LogView.as_view(),name="log"),
    path('logout/',LogOutView.as_view(),name="logout"),

]
