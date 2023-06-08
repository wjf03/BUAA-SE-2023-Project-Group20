from django.shortcuts import render
import json
from book.models import Book
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def addBook(request):
    if request.method == 'POST':
        # 检测 POST 类型的请求

        data_json = json.loads(request.body)
        # 此时 data_json 已经转为了字典类型

        book_name = data_json['book_name']
        book_introduction = data_json['book_introduction']
        book_main_type = data_json['book_main_type']
        book_secondary_type = data_json['book_secondary_type']
        book_author_name = data_json['book_author_name']
        book_popularity = data_json['book_popularity']
        book_score = data_json['book_score']
        book_url = data_json['book_url']

        book = Book(book_name=book_name, book_introduction=book_introduction, book_main_type=book_main_type, 
        book_secondary_type=book_secondary_type, book_author_name=book_author_name, book_popularity=book_popularity, 
        book_score=book_score, book_url=book_url)
        # id 是自动赋值，不需要指明
        # post 不赋值会使用默认值0

        book.save()
        return JsonResponse({'result': 1, 'message': '添加成功!'})

@csrf_exempt
def deleteBook(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    id = data_json["book_id"]
    if Book.objects.filter(book_id=id).exists() == True:
        book = Book.objects.get(book_id=id)
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    book.delete()
    return JsonResponse({'result': 1, 'message': '删除成功!'})

@csrf_exempt
def modifyBook(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    id = data_json["book_id"]
    if Book.objects.filter(book_id=id).exists() == True:
        book = Book.objects.get(book_id=id)
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    name = data_json["book_name"]
    intro = data_json["book_introduction"]
    main = data_json["book_main_type"]
    sec = data_json["book_secondary_type"]
    author = data_json["book_author_name"]
    book.book_name = name
    book.book_introduction = intro
    book.book_main_type = main
    book.book_secondary_type = sec
    book.book_author_name = author
    book.save()
    return JsonResponse({'result': 1, 'message': '修改成功!'})

@csrf_exempt
def BookPopularityAdd(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    id = data_json["book_id"]
    if Book.objects.filter(book_id=id).exists() == True:
        book = Book.objects.get(book_id=id)
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    book.book_popularity += 1
    book.save()
    return JsonResponse({'result': 1, 'message': '修改成功!'})

@csrf_exempt
def modifyScore(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    id = data_json["book_id"]
    if Book.objects.filter(book_id=id).exists() == True:
        book = Book.objects.get(book_id=id)
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    score = data_json["book_score"]
    book.book_score =score
    book.save()
    return JsonResponse({'result': 1, 'message': '修改成功!'})

@csrf_exempt
def getBookById(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    id = data_json["book_id"]
    if Book.objects.filter(book_id=id).exists() == True:
        book = Book.objects.get(book_id=id)
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    return JsonResponse({'result': 1, "message": '成功！', 'post': book.to_dic()})

@csrf_exempt
def getBookByAuthor(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    author = data_json["book_author_name"]
    if Book.objects.filter(book_author_name=author).exists() == True:
        books = [{
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_introduction': x.book_introduction,
            'book_main_type': x.book_main_type,
            'book_secondary_type': x.book_secondary_type,
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_author_name': x.book_author_name,
            'book_popularity': x.book_popularity,
            'book_score': x.book_score,
        } for x in Book.objects.order_by('book_popularity').filter(book_author_name=author)]
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    return JsonResponse({'result': 1, "message": '成功！', 'posts': books})

@csrf_exempt
def getBookByMainType(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    main = data_json["book_main_type"]
    if Book.objects.filter(book_main_type=main).exists() == True:
        books = [{
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_introduction': x.book_introduction,
            'book_main_type': x.book_main_type,
            'book_secondary_type': x.book_secondary_type,
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_author_name': x.book_author_name,
            'book_popularity': x.book_popularity,
            'book_score': x.book_score,
        } for x in Book.objects.order_by('book_popularity').filter(book_main_type=main)]
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    return JsonResponse({'result': 1, "message": '成功！', 'posts': books})

@csrf_exempt
def getBookByTwoType(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    main = data_json["book_main_type"]
    sec = data_json["book_secondary_type"]
    if Book.objects.filter(book_main_type=main).filter(book_secondary_type=sec).exists() == True:
        books = [{
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_introduction': x.book_introduction,
            'book_main_type': x.book_main_type,
            'book_secondary_type': x.book_secondary_type,
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_author_name': x.book_author_name,
            'book_popularity': x.book_popularity,
            'book_score': x.book_score,
        } for x in Book.objects.order_by('book_popularity').filter(book_main_type=main).filter(book_secondary_type=sec)]
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    return JsonResponse({'result': 1, "message": '成功！', 'posts': books})

@csrf_exempt
def searchBookByKey(request):
    if request.method != 'POST':
        return JsonResponse({'result': 0, 'message': 'request error!'})
    data_json = json.loads(request.body)
    key = data_json['key']
    books = [{
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_introduction': x.book_introduction,
            'book_main_type': x.book_main_type,
            'book_secondary_type': x.book_secondary_type,
            'book_id': x.book_id,
            'book_name': x.book_name,
            'book_author_name': x.book_author_name,
            'book_popularity': x.book_popularity,
            'book_score': x.book_score,
        } for x in Book.objects.order_by('book_popularity').filter(book_name__contains=key)]
    return JsonResponse({'result': 1, "message": '成功！', 'posts': books})
  
@csrf_exempt
def getBookSource(request):
    data_json = json.loads(request.body)
    id = data_json['id']
    if Book.objects.filter(book_id=id).exists() == True:
        book = Book.objects.get(book_id=id)
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    url = book.book_url
    return JsonResponse({'result': url, 'message': '成功!'})
    # data_json = json.loads(request.body)
    # path = data_json['path']
    # if os.path.exists(path):
    #     with open(path, 'rb') as f:
    #         file_data = f.read()
    #     response = HttpResponse(file_data, content_type='application/octet-stream')
    #     response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(path))
    #     return response
    # else:
    #     return HttpResponse("Sorry, the file you requested does not exist.")

@csrf_exempt
def getBookId(request):
    data_json = json.loads(request.body)
    name = data_json['book_name']
    if Book.objects.filter(book_name=name).exists() == True:
        book = Book.objects.get(book_name=name)
    else:
        return JsonResponse({'result': 0, 'message': '图书不存在!'})
    id = book.book_id
    return JsonResponse({'result': id, 'message': '成功!'})