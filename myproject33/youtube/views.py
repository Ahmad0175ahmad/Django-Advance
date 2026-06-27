from django.shortcuts import render
from .models import YouTubeUser
from django.core.cache import cache
# Create your views here.

def users_list(request):
    users=cache.get('users_data') #Try to get data from cache

    if not users:
        print("Cache miss: Fetching data from database")
        users =YouTubeUser.objects.all()
        cache.set('users_data',users, timeout=60)
    else:
        print("Cache hit: Fetching data from cache")

    return render(request, 'users_list.html', {'users': users})   

