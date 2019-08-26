from datetime import datetime
import time

from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
import  random,string


# Create your views here.
from loginapp.captcha.image import ImageCaptcha
from loginapp.models import User


def cook(request):
    print('来过cook')
    name = request.COOKIES.get('name')
    pwd = request.COOKIES.get('pwd')
    result = User.objects.filter(name=name, password=pwd)
    request.session['login'] = None
    if result:
        return HttpResponse('ok')

    return HttpResponse('no')



def fn_login(request):

    name=request.GET.get('name')
    pwd=request.GET.get('pwd')
    rem=request.GET.get('rember')
    print(rem,'%%%%%%%%%%%%%%')
    result=User.objects.filter(name=name,password=pwd)
    if result:
        res=HttpResponse('ok')
        if rem:
            res.set_cookie('name',name, max_age=7*24*3600)
            res.set_cookie('pwd',pwd,max_age=7*24*3600)
        request.session['login']='ok'
        return res
    else:
        return HttpResponse('no')






def fn_regist(request):
    name1= request.GET.get('username')
    name2=request.GET.get('name')
    pwd = request.GET.get('pwd')
    gender=request.GET.get('sex')
    code1=request.GET.get('number')
    User.objects.create(name=name1, uname=name2, password=pwd, gender=gender, code=code1)
    re = HttpResponse('ok')
    re.set_cookie('name', None)
    re.set_cookie('pwd', None)
    return re



def getcaptcha(request):
    image = ImageCaptcha()
    codes1 = random.sample(string.ascii_lowercase+string.digits, 4)
    codes = ''.join(codes1)
    data = image.generate(codes)
    # print(codes)
    request.session['code'] = codes
    return HttpResponse(data, 'image/png')

def getcaptcha_ajax(request):
    time.sleep(3)
    code2=request.session.get('code')
    code=request.GET.get('code')

    if code2.lower() == code.lower():
        return HttpResponse("yes")

    return HttpResponse("no")

def registajax(request):
    time.sleep(3)

    name= request.GET.get('name')

    result=User.objects.filter(name=name)
    if result:
        return HttpResponse('yes')
    return HttpResponse('no')

