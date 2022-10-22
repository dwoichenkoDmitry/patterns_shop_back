from django.shortcuts import render
from .models import ProbImg
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .serializers import ImageSerializer


@api_view(['POST'])
def SaveIm(request):
        image = ProbImg(image=request.data['photo'])
        image.save()
        return Response({'data': image})


@api_view(['GET'])
def GetIm(request):
        image = ProbImg.objects.all()
        print(image[0])
        return Response({'data': 'ok'})

class ImageViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put']
    queryset = ProbImg.objects.all()
    serializer_class = ImageSerializer
    pagination_class = None