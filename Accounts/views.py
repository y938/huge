from django.shortcuts import render,redirect

from .form import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib import auth


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user + ' successfully!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'earth/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username, password=password, email=email)

        if user is not None:
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('home')

        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'earth/login.html', context)


def logoutUser(request):
    auth.logout(request)
    return redirect('/')

