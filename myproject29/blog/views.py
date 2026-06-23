from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookie(request):
    response=HttpResponse("Cookie Set Successfully")
    response.set_cookie('username','Ahmad', max_age=60*60*24)
    response.set_cookie('course','Django',max_age=60*60*24)
    return response

def get_cookie(request):
    username=request.COOKIES.get('username','Guest')
    course=request.COOKIES.get('course','No Course Selected')
    if 'username' in request.COOKIES:
        return HttpResponse(f"Username : {username}, Course: {course}")
    else:
        return HttpResponse("No Cookies found")

def delete_cookie(request):
    response=HttpResponse("Cookie Deleted Successfully")
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response