from django.shortcuts import render
import json
from author.models import Author
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add_author(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        name = data_json['name']
        introduction = data_json['introduction']
    
        author = Author(name=name,introduction=introduction)
        
        author.save()
        return JsonResponse({'result': 1, 'message': '添加成功'})
    
@csrf_exempt
def delete_author(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        author_id = data_json['id']
        
        try:
            author = Author.objects.get(id=author_id)
            author.delete()
            return JsonResponse({'result': 1, 'message': '删除成功'})
        except Author.DoesNotExist:
            return JsonResponse({'result': 0, 'message': '作者不存在'})
        
@csrf_exempt
def edit_author(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        author_id = data_json['id']
        introduction = data_json['introduction']
        
        try:
            author = Author.objects.get(id=author_id)
            author.introduction = introduction
            author.save()
            return JsonResponse({'result': 1, 'message': '编辑成功'})
        except Author.DoesNotExist:
            return JsonResponse({'result': 0, 'message': '作者不存在'})
        
@csrf_exempt
def search_author(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        name = data_json['name']  # 假设前端传递的数据包含要搜索的作者的名字
        
        if Author.objects.filter(name=name).exists() == True:
            author = Author.objects.get(name=name)
            return JsonResponse({'result': 1, 'message': '查询成功', 'author': author.to_dic()})
        else:
            return JsonResponse({'result': 0, 'message': '未找到匹配的作者'})