from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Courses

# Create your views here.
@api_view(['POST'])
def AddCourse(request):
    name = request.data['name']
    link = request.data['link']
    image = request.data['image']

    Courses(name=name, link=link, image=image).save()
    return Response({'answer': 'created'})

@api_view(['POST'])
def DeleteCourse(request):
    id = request.data['id']

    Courses.objects.filter(id=id).delete()
    return Response({'answer': 'deleted'})

@api_view(['POST'])
def UpdateCourse(request):
    id = request.data['id']
    name = request.data['name']
    link = request.data['link']
    image = request.data['image']

    course = Courses.objects.filter(id=id)[0]
    if(course.name!=name):
        course.name = name
    if(course.link!=link):
        course.link = link
    if(course.image!='' and course.image!=image):
        course.image = image

    course.save()
    return Response({'answer': 'updated'})

@api_view(['GET'])
def GetAllCourses(request):
    courses = Courses.objects.all()
    mas = []
    for item in courses:
        mas.append(
            {
                'id': item.id,
                'name': item.name,
                'link': item.link,
                'image': str(item.image)
            }
        )

    return Response({'courses': mas})