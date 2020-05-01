from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm


# imports for user authnetication login/logout

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html', context=None)

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # we are not saving profile info since one-to-one relationship to the extra profile attributes with the original User model
            profile = profile_form.save(commit=False)
            profile.user = user

            # Check whether there is a uploaded profile pic. 'profile_pic' is the attribute defined in models.py
            # Checking "request.FILES" is required this will have the uploaded contents like images, csv files and etc
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # the keys in the content dict are used in registration.html
    content = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, 'basic_app/registration.html', context=content)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # a single line of code authenticate the login details i.e username and password. if
        user = authenticate(username=username, password=password)

        if user:    # if user is not None;
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {}, password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'basic_app/login.html', context=None)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')
