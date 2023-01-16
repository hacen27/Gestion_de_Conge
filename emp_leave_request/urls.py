from django.urls import path
from .views import leave_request_form, leave_request_list, home,signup_view,login_view

urlpatterns = [
     path('register/', signup_view, name='signup'),
     path('',login_view, name='login'),
    path('leave_request_form/', leave_request_form, name='leave_request_form'),
    path('leave_request_list/', leave_request_list, name='leave_request_list'),
    path('home/', home, name='home')

]

