from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from UserProfile.models import UserProfile
import random



def index(request):    
    title = {'title': "Home"}
    return render(request, 'index.html', title)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        valid_user = authenticate(
            request, username=username, password=password)
        if valid_user is not None:
            auth_login(request, valid_user)
            return redirect(reverse_lazy('UserProfile:index'))
        else:
            return HttpResponse("wrong informations")

    return render(request, 'UserProfile/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('UserProfile:index'))



def registrations(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Password = request.POST.get('password')
        Password2 = request.POST.get('password2')
        DateOfBirth = request.POST.get('DateOfBirth')
        profession = request.POST.get('profession')
        bloodGroup = request.POST.get('bloodGroup')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        thana = request.POST.get('thana')
        union = request.POST.get('union')
        postCode = request.POST.get('postCode')
        # bio=" "

        check_user = User.objects.filter(email=email).first()
        check_profile = UserProfile.objects.filter(phone=phone).first()

        if Password != Password2:
            context1 = {"message1": "Password mismatch", "class1": "danger"}
            return render(request, 'UserProfile/registration.html', context1)

        if check_user or check_profile:
            context = {"message": "User already exist", "class": "danger"}
            return render(request, 'UserProfile/registration.html', context)

        user = User.objects.create_user(
            first_name=fname, last_name=lname, username=username, email=email, password=Password)
        user.save()

        profile= UserProfile(user=user,
                              phone=phone, DateOfBirth=DateOfBirth,
                              profession=profession,
                              bloodGroup=bloodGroup,
                              gender=gender,
                              city=city,
                              thana=thana,
                              union=union,
                              postCode=postCode,
        )
        profile.save()

        context = {"message": "Successfully registrations Complate",
                    "class2":"alert1 success ",
                   }
        return render(request, 'UserProfile/login.html', context)

    return render(request, 'UserProfile/registration.html')

def user_profile(request,username):
    user_information=get_list_or_404(User, username=username)
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_profile_info=UserProfile.objects.get(user__pk=user_id)
        img=user_profile_info.profile_pic
        print(img)

    context={"title":"Profile", "user_information":user_information,"user_profile_info":user_profile_info}

    return render(request, 'UserProfile/Profile.html', context)


def update_profile(request,username):
    user_information=get_list_or_404(User, username=username)
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_profile_info=UserProfile.objects.get(user__pk=user_id)
        user_profile_info_id=user_profile_info.id

    if(request.method=="POST" and request.FILES):
        username=request.POST.get("username")
        phone=request.POST.get("phone")
        bio=request.POST.get("bio")
        city=request.POST.get("address")
        profile_picture=request.FILES['profile_picture']

        User_Profile=UserProfile(user=current_user, profile_pic=profile_picture)
        User_Profile.save()
        User.objects.filter(id=user_id).update(username=username)
        UserProfile.objects.filter(pk=user_profile_info_id).update(
            phone=phone,
            city=city,
            )
        return redirect(reverse_lazy('UserProfile:index'))

    context={"title":"Profile", "user_information":user_information,"user_profile_info":user_profile_info}
    return render(request, 'UserProfile/UpdateProfile.html',context)


def search_donor(request):
    userprofile=UserProfile.objects.all()
    if request.method=="POST":
        blood_group=request.POST.get("blood")
        location=request.POST.get("location")
        
        userprofile=UserProfile.objects.filter(
            bloodGroup__contains=blood_group,
            city__contains=location,
        )

        context={'userprofile':userprofile}
        return render(request, 'UserProfile/search.html',context)
    context={'userprofile':userprofile}
    return render(request, 'UserProfile/search.html',context)


def About_Blood(request):
    title = {'title': "About Blood"}
    return render(request, 'about_blood.html',title)
