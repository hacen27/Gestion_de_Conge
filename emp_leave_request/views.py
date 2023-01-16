
from .models import Employee, LeaveRequest
from .forms import LeaveRequestForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            try:
                User = get_user_model()
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                login(request, user)
                return redirect('login')
            except:
                return render(request, 'signup.html', {'error': 'An error occurred while creating your account'})
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

def home(request):
    return render(request, 'leave_request/home.html')



def leave_request_form(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee=Employee.objects.get(user=request.user)
            # leave_request.employee = request.user
            leave_request.save()
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm()

    context = {'form': form}
    return render(request, 'leave_request/leave_request_form.html', context)



def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all()
    print("**********************liste de leave request************************")
    context = {'leave_requests': leave_requests}

    return render(request, 'leave_request\leave_request_list.html', context)