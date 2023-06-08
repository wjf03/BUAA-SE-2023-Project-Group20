from django.shortcuts import render
import json
from user.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # 检测 POST 类型的请求

        data_json = json.loads(request.body)
        # 此时 data_json 已经转为了字典类型

        username = data_json['username']
        password = data_json['password']
        ifManager = data_json['ifManager']
        # 不确定是否有这个参数，使用get
        if User.objects.filter(username=username).exists() == True:
            return JsonResponse({'result': 0, 'message': '用户名已存在!'})
        user = User(username=username, password=password, ifManager=ifManager)
        # id 是自动赋值，不需要指明
        # post 不赋值会使用默认值0

        user.save()
        return JsonResponse({'result': 1, 'message': '注册成功!'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        username = data_json['username']
        password = data_json['password']
        if User.objects.filter(username=username).exists() == True:
            # 使用 filter 先检查存在性
            user = User.objects.get(username=username)
        else:
            return JsonResponse({'result': 0, 'message': '用户不存在!'})
                # 查询语句，根据括号中的条件，返回唯一一条结果
                # 如果有多个表项匹配这一条件，则报错

        if user.password == password:
            return JsonResponse({'result': user.user_id, 'message': '登录成功!'})
        else:
            return JsonResponse({'result': 0, 'message': '密码错误!'})

@csrf_exempt
def logout(request):
    data_json = json.loads(request.body)
    id = data_json["user_id"]
    if id != 0:
        # 清空所有的信息
        return JsonResponse({'result': 1, 'message': r'已登出!'})
    else:
        return JsonResponse({'result': 0, 'message': r'请先登录!'})

@csrf_exempt
def modifyUser(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        id = data_json["user_id"]
        if User.objects.filter(user_id=id).exists() == True:
            user = User.objects.get(user_id=id)
        else:
            return JsonResponse({'result': 0, 'message': '用户不存在!'})
        name = data_json['username']
        if User.objects.filter(username=name).exists() == True:
            user2 = User.objects.get(username=name)
            if user2.user_id != user.user_id:
                return JsonResponse({'result': 0, 'message': '用户名已存在!'})
        sex = data_json['sex']
        user.username = name
        user.sex = sex
        user.save()
        return JsonResponse({'result': 1, 'message': '修改成功!'})

@csrf_exempt
def getUser(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        id = data_json["user_id"]
        if User.objects.filter(user_id=id).exists() == True:
            user = User.objects.get(user_id=id)
        else:
            return JsonResponse({'result': 0, 'message': '用户不存在!'})
        name = user.username
        flag = user.ifManager
        return JsonResponse({'result': {"name": name, "ifManager": flag}, 'message': '返回成功！'})

@csrf_exempt
def getManager(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        id = data_json["user_id"]
        if User.objects.filter(user_id=id).exists() == True:
            user = User.objects.get(user_id=id)
        else:
            return JsonResponse({'result': 0, 'message': '用户不存在!'})
        flag = user.ifManager
        return JsonResponse({'result': flag, 'message': '返回成功！'})