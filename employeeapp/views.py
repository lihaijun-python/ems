import os
import uuid
from datetime import datetime
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django_redis.serializers import json

from employeeapp.models import Employee
# def update(request):
#     page = request.GET.get('page')
#     request.session['page1'] = page
#     a = int(request.GET['id'])
#     m=Employee.objects.get(id=a)
#     # e = Employee.objects.get(id=a)
#     # e.delete()
#     return render(request, 'employeeapp/updateEmp.html',{'m':m,'page':page})

def update_emp(request):
    user_id = request.POST.get('id')
    print(user_id,'==============')
    if user_id:
        def mydefault(emp):
            if isinstance(emp,Employee):
                return {'id':emp.id,'name':emp.name,'age':emp.age,'salary':str(emp.salary),'birthday':emp.birthday.strftime('%Y-%m-%d'),'headpic':emp.headpic.url}
        user = Employee.objects.get(id=user_id)
        return JsonResponse({"user": user}, json_dumps_params={"default":mydefault })
    return HttpResponse('error')


def fn_update(request):
    print('进入更新函数')
    id = request.POST.get('id')
    print(id,'-----------')
    name = request.POST.get('name')
    print(name,'===========')
    salary = request.POST.get('salary')
    print(salary)

    age = request.POST.get('age')
    print(age)
    birthday = request.POST.get('birthday')
    print(birthday)
    file = request.FILES.get('png')
    print(file)
    emp = Employee.objects.get(pk=id)
    emp.name = name
    emp.salary = salary
    emp.age = age
    emp.birthday = birthday
    if file:
        emp.headpic = file

    emp.save()
    return HttpResponse('ok')
    # except:
    #     return HttpResponse('error')




def fn_add(request):
    name=request.POST.get("name")#获取用户名
    print(name)

    salary=request.POST.get("salary" )#获取工资
    print(salary)
    age= request.POST.get("age")#获取年龄
    print(age)

    birthday=request.POST.get('birthday')
    print(birthday)
    file = request.FILES.get('source')
    print(file)
    request.session['page1']='a'
    Employee.objects.create(name=name,salary=salary,age=age,birthday=birthday,headpic=file)

    return HttpResponse('ok')

def dele(request):
    # page=request.GET.get('page')
    # print(page)
    # request.session['page1']=page

    a = int(request.GET['id'])
    if a:
        e = Employee.objects.get(id=a)
        e.delete()

        return HttpResponse('ok')
    else:
        return HttpResponse('no')




# def home(request):
#     time = datetime.now()
#     result=request.session.get('login')
#     if result:
#         number = request.GET.get('page',1)
#         p1= request.session.get('page1')
#         request.session['page1']=None
#         users = Employee.objects.all()
#         pagtor = Paginator(users, per_page=2)
#         p=pagtor.num_pages
#
#
#         # if not number:#如果没有获取前端的页面从新赋值
#         #     number=1
#
#         page=pagtor.page(number)
#         if p1:
#             if p1 == 'a'or int(p1)>p:#判断当session里的值等于a或当session值大于最大页面将最大页面值传入器前端
#                 page=pagtor.page(p)
#             else:
#                 page=pagtor.page(p1)#如果不是传session值
#         return render(request, 'employeeapp/emplist.html', {'page': page,'time':time})
#
#
#     return redirect("loginapp:login")
def sess(request):
    print('*******************')
    result = request.session.get('login')
    if result:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

def query(request):
    result = request.session.get('login')
    if result:
        def user_default(u):
            if isinstance(u,Employee):
                return {'id':u.id,'name':u.name,'age':u.age,'salary':str(u.salary),'birthday':u.birthday.strftime('%Y-%m-%d'),'headpic':u.headpic.url}
        user = list(Employee.objects.all())
        return JsonResponse({"users":user},json_dumps_params={"default":user_default})


