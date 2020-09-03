from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view
from app.models import Student
from app.serializers import StudentSerializer
from rest_framework.decorators import api_view
from django.db.models.functions import Lower

# Create your views here.
@api_view(['POST'])
def student_add(request):
    # add student
    req = JSONParser().parse(request)
    student_serializer = StudentSerializer(data=req)

    if not student_serializer.is_valid():
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    student_serializer.save()        
    return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def student_list(request):
    # get student list
    req = JSONParser().parse(request)
    offset, limit, order_by, order_dir = req['offset'], req['limit'], req['order_by'], req['order_dir']

    if not limit or not order_by or not order_dir:
        return JsonResponse({'message': 'invalid param'}, status=status.HTTP_400_BAD_REQUEST)

    students = Student.objects.all().order_by(Lower(order_by).desc() if order_dir == 'desc' else Lower(order_by).asc())[offset:offset+limit]
    student_serializer = StudentSerializer(students, many=True)

    return JsonResponse(student_serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def student(request,id):
    # get student detail by id
    try: 
        student = Student.objects.get(pk=id) 
    except Student.DoesNotExist: 
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # query detail by id
    if request.method == 'GET':
        student_serializer = StudentSerializer(student)
        return JsonResponse(student_serializer.data, status=status.HTTP_200_OK)
    
    # query update by id
    elif request.method == 'PUT':
        req = JSONParser().parse(request)
        student_serializer = StudentSerializer(student,data=req)
        if not student_serializer.is_valid():
            return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        student_serializer.save() 
        return JsonResponse(student_serializer.data, status=status.HTTP_200_OK)

    # query delete by id
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'The student succesfully delete'}, status=status.HTTP_200_OK)