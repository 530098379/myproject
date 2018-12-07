import json

from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.db import connection
from myapp.models import Book
from myapp.tool import dict_fetchall


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        timers = Book.objects.order_by('time_stamp')[:5]
        response['list'] = json.loads(serializers.serialize("json", timers))

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_log(request):
    file_name = request.GET.get('content', default='')
    response = {}
    try:
        log_str = ''
        log_arr = []
        file_path = 'C:\Work\doc\\' + file_name
        with open(file_path, 'r', encoding='utf-8') as file_object:
            lines = file_object.readlines()
        for line in lines:
            log_str += line.rstrip()
            log_str += '\n'
            log_arr.append(line.rstrip())

        response['log_arr'] = log_arr
        response['file_name'] = file_name

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def execute_sql(request):
    sql_text = request.GET.get('title', default='')
    response = {}
    cursor = connection.cursor()
    try:
        cursor.execute(sql_text)
        response['list'] = dict_fetchall(cursor)

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    finally:
        cursor.close()

    return JsonResponse(response)
