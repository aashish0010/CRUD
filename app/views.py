from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import io
from .models import Crud
from .serializers import CrudSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            crud = Crud.objects.get(id=id)
            serializer = CrudSerializer(crud)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        crud = Crud.objects.all()
        serializer = CrudSerializer(crud, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = CrudSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "Data Created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        crud = Crud.objects.get(id=id)
        serializer = CrudSerializer(crud, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated !!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        crud = Crud.objects.get(id=id)
        crud.delete()
        res = {'msg': 'Data Deleted !!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
