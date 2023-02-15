from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse


# Create your views here.


def show(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailid = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password2 == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect(reverse('registration:show'))
            elif User.objects.filter(email=emailid).exists():
                messages.info(request, "email is already exists")
                return redirect(reverse('registration:show'))
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=emailid,
                                                password=password1, )
                user.save()
                print("created")
                return redirect(reverse('registration:log'))
        else:
            messages.info(request, "password does not mach")
            return redirect(reverse('registration:show'))
        return redirect('log')

    return render(request, 'registration.html')


def log(request):
    if request.method == 'POST':
        lusername = request.POST['lusername']
        lpassword = request.POST['lpassword']
        user = auth.authenticate(username=lusername, password=lpassword)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return redirect(reverse('registration:log'))

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
