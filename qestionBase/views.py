from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Question


# Create your views here.
@api_view(['POST'])
def SaveQuestion(request):
        Question(first_name=request.data['name'], wayCalling=request.data['type'],
                 callRealize=request.data['realise'], questionText=request.data['message']).save()
        return Response({'data': "ok"}, status=status.HTTP_201_CREATED)


@api_view(['Get'])
def GetAllQuestions(request):
    questions = Question.objects.all()
    mas = []
    for item in questions:
        mas.append({
            'name': item.first_name,
            'way': item.wayCalling,
            'realize': item.callRealize,
            'text': item.questionText
        })

    return Response({'data': mas})


@api_view(['POST'])
def DeleteQuestion(request):
    realize = request.data['realize']
    text = request.data['text']
    name = request.data['name']

    Question.objects.filter(first_name=name, callRealize=realize, questionText=text).delete()
    return Response({'data': 'deleted'})