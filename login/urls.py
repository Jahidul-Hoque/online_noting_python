from login import views
from django.urls import path
app_name="login"

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('',views.applogin,name='applogin'),
    path('logout/',views.logout_user,name='logout_user'),
    path('yourprofile/',views.profile,name='profile'),
    path('addphoto/',views.add_pro_pic,name='add_pro_pic'),

]
