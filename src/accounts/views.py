from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import logout


# Create your views here.
def signup_view(request):  #get ali post request. get če link vtipkalo
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # valid or invalid result
        if form.is_valid():
            user = form.save()  # save to db
            # log the user in
            login(request, user)
            return redirect('http://127.0.0.1:8000/index.html')
        # if get request send blank form
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form': form })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log user in
            user = form.get_user()
            login(request, user)
            return render(request, 'index.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
        logout(request)
        return render(request, 'index.html')