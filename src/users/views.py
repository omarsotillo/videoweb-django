from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Videos


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You are successfully logged in " + user.get_username() + "!"
                print ("User with username %s and password %s is active, valid and authenticated" % (
                    username, password))
            else:
                state = "Your account is not active , please contact the site admin"
                print ("User with username %s and password %s is inactive" %
                       (username, password))
        else:
            state = "Your username or password were incorrect."
            print ("User with username %s and password %s failed to login. Wrong username or password" % (
                username, password))

    return render(request, 'login.html', {'state': state, 'username': username})


def index(request):
    username = password = first_name = last_name = email = ''
    video_list = Videos.objects.all().filter(private=False)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        print ("New user created with the following data. %s %s %s %s %s " %
               (username, password, first_name, last_name, email))
        user = User.objects.create_user(
            username=username, email=email, password=password, last_name=last_name, first_name=first_name)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You are successfully logged in " + user.get_username() + "!"
                print ("User with username %s and password %s is active, valid and authenticated" % (
                    username, password))
            else:
                state = "Your account is not active , please contact the site admin"
                print ("User with username %s and password %s is inactive" %
                       (username, password))
        else:
            state = "Your username or password were incorrect."
            print ("User with username %s and password %s failed to login. Wrong username or password" % (
                username, password))

    return render(request, 'index.html', {'video_list': video_list})


def logout_user(request):
    if request.user.is_authenticated():
        state = "You are no more logged to this web page " + \
            request.user.get_username() + "."
        logout(request)
    else:
        state = "You first need to login to access this place."

    return render(request, 'logout.html', {'state': state})


def modify_user(request):
    username = email = first_name = last_name = ''
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = request.user
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
    return render(request, "modify.html")


def newvideo(request):
    name = description = tags = ''
    if request.POST:
        user = request.user
        name = request.POST.get('name')
        description = request.POST.get('description')
        tags = request.POST.get('tags')
        video_file = request.FILES.get('file')
        video_object = Videos.objects.create(
            user=user, description=description, name=name, tags=tags)
        print("%s %s %s %s" % (user.username, name, description, tags))

    return render(request, 'newvideo.html')


def profile(request):
    if request.user.is_authenticated():
        video_list = Videos.objects.filter(user=request.user)
        return render(request, 'profile.html', {'video_list': video_list})
    else:
        return render(request, 'profile.html')


def search(request):
    tag = ''
    if request.POST and 'tags' in request.POST:
        tag = request.POST.get('tag')
        video_list = Videos.objects.filter(tags__icontains=tag ,private=False)
        return render(request, 'search.html', {'video_list': video_list})
    if request.POST and 'name' in request.POST:
        tag = request.POST.get('tag')
        video_list = Videos.objects.filter(name__icontains=tag,private=False)
        return render(request, 'search.html', {'video_list': video_list})
    else:
        return render(request, 'search.html')


def videos(request, id):
    video_list = Videos.objects.filter(id=id)
    for video in video_list:
        video.views = video.views + 1
        video.save()

    if request.POST and 'upvote' in request.POST:
        for video in video_list:
            video.upvotes = video.upvotes + 1
            video.views = video.views - 1
            video.save()

    if request.POST and 'downvote' in request.POST:
        for video in video_list:
            video.downvotes = video.downvotes + 1
            video.views = video.views - 1
            video.save()

    return render(request, 'video.html', {'video_list': video_list})


def delete(request, id):
    video_list = Videos.objects.filter(id=id)
    for video in video_list:
        if request.user == video.user:
            video.delete()

    return render(request, 'profile.html', {'video_list': video_list})


def contact(request):
    return render(request, 'contact.html', {'video_list': video_list})
