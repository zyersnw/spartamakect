
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from products.models import Item, Favorite
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    if request.user.is_authenticated:
        welcome_message = f"{request.user.username} 님, 환영합니다!"
    else:
        welcome_message = ""

    return render(request, 'home.html', {'welcome_message': welcome_message})
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('login') 
    else:
        return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, '로그인에 성공했습니다. 환영합니다!')
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, '로그인에 실패했습니다. 아이디와 비밀번호를 다시 확인해주세요.')
            return redirect('login') 
    else:
        return render(request, 'login.html')
    
    
def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})


def user_logout(request):
    logout(request)
    return redirect('home')

from django.http import HttpResponseRedirect
from django.urls import reverse

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    items_registered = Item.objects.filter(seller=user)
    
    favorites = Favorite.objects.filter(user=user)
    items_favorited = [favorite.item for favorite in favorites]
    
    followed = False
    following_count = 0
    followers_count = 0
    if hasattr(user, 'profile'):
        if request.user.is_authenticated:
            followed = request.user.profile.following.filter(id=user_id).exists()
        following_count = user.profile.following.count()
        followers_count = user.profile.followers.count()
    
    if request.method == 'POST':
        followed_user = get_object_or_404(User, pk=request.POST.get('user_id'))
        if request.user != followed_user:
            if followed:
                request.user.profile.following.remove(user.profile)
            else:
                request.user.profile.following.add(user.profile)
        return HttpResponseRedirect(reverse('profile', args=[user_id]))
    
    return render(request, 'profile.html', {'user': user, 'items_registered': items_registered, 'items_favorited': items_favorited, 'following_count': following_count, 'followers_count': followers_count, 'followed': followed})